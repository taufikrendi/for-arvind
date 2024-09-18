import datetime

from asgiref.sync import sync_to_async

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse, Http404

from deposits.models import DepositMemberPrincipal, DepositMemberMandatory
from transaction.models import TransactionDepositVerified


@sync_to_async
@receiver(post_save, sender=TransactionDepositVerified, dispatch_uid="approval_transactions_deposit")
def approval_transactions_deposit(sender, instance, created, **kwargs):
    if not created:
        if instance.get_choice == 'Approval.AP':
            TransactionDepositVerified.objects.using('transaction_master').filter(
                transaction_deposit_verified_transit_code=instance.code_id
            ).update(
                transaction_deposit_verified_approval_status=True,
                transaction_deposit_verified_created_by_admin=instance.user,
                transaction_deposit_verified_created_date_admin=datetime.datetime.now()
            )
            DepositMemberPrincipal.objects.using('funds_master').filter(
                deposit_member_principal_user_related=instance.member_id
            ).update(
                deposit_member_principal_payment_transaction_number=instance.code_id,
                deposit_member_principal_payment_principal_status=True,
                deposit_member_principal_payment_principal_amount=instance.for_principal_amount
            )
            DepositMemberMandatory.objects.using('funds_master').filter(
                deposit_member_mandatory_user_related=instance.member_id
            ).update(
                deposit_member_mandatory_amount=instance.for_mandatory_amount,
                deposit_member_mandatory_period_left=instance.left,
                deposit_member_mandatory_period_end=instance.end_date,
                deposit_member_mandatory_updated_by=instance.user,
                deposit_member_mandatory_updated_date=datetime.datetime.now()
            )
        else:
            TransactionDepositVerified.objects.using('transaction_master').filter(
                transaction_deposit_verified_transit_code=instance.code_id
            ).update(
                transaction_deposit_verified_approval_status=False,
                transaction_deposit_verified_created_by_admin=instance.user,
                transaction_deposit_verified_created_date_admin=datetime.datetime.now()
            )
    else:
        return HttpResponse("Error Approval Transaction")