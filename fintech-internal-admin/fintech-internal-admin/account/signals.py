import datetime

from asgiref.sync import sync_to_async

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse, Http404

from account.models import AccountProfile, AccountMemberVerifyStatus


@sync_to_async
@receiver(post_save, sender=AccountMemberVerifyStatus, dispatch_uid="approval_member")
def approval_member(sender, instance, created, **kwargs):
    if not created:
        AccountMemberVerifyStatus.objects.using('default').filter(
            account_member_verify_status_user_related=instance.get_member
        ).update(
            account_member_verify_status_profile_close_to_update=True,
            account_member_verify_status_revision_profile_check=True,
            account_member_verify_status_revision_profile_last_date=datetime.datetime.now(),
            account_member_verify_status_updated_by=instance.user
        )
        AccountProfile.objects.using('default').filter(
            account_profile_user_related=instance.get_member
        ).update(
            account_profile_cooperative_number=int(float(datetime.datetime.now().timestamp()) * 100)
        )
    else:
        return HttpResponse("Error Approval Member")
