from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Q
from django.db.models.signals import post_save
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from deposits.models import DepositMemberPrincipal, DepositMemberMandatory
from transaction.models import *
from transaction.signals import approval_transactions_deposit
from utils.forms import ApprovalForm
from utils.validators import get_user


@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
def all_transaction(request):
    data = TransactionDepositVerified.objects.using('transaction_slave').raw(
    "select transaction_transactiondepositverified.transaction_deposit_verified_id,"
    "transaction_transactiondeposittransit.transaction_deposit_transit_id,"
    "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_id,"
    "transaction_transactiondepositverified.transaction_deposit_verified_transit_code,"
    "transaction_transactiondepositverified.transaction_deposit_verified_user_related,"
    "transaction_transactiondeposittransit.transaction_deposit_transit_gt_amount,"
    "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_amount,"
    "transaction_transactiondeposittransit.transaction_deposit_transit_type, "
    "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_type, "
    "transaction_transactiondepositverified.transaction_deposit_verified_status "
    "from transaction_transactiondepositverified "
    "left join transaction_transactiondeposittimetransit on "
    "transaction_transactiondepositverified.transaction_deposit_verified_transit_code="
    "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_code "
    "left join transaction_transactiondeposittransit on "
    "transaction_transactiondepositverified.transaction_deposit_verified_transit_code="
    "transaction_transactiondeposittransit.transaction_deposit_transit_code "
    "where transaction_deposit_verified_approval_status=False "
    "order by transaction_transactiondepositverified.transaction_deposit_verified_created_date")

    search = request.POST.get('search')

    if search:
        data = data.filter(Q(email__contains=search))
    else:
        data.using('transaction_slave')

    page = request.GET.get('page', 1)
    paginator = Paginator(data.using('transaction_slave'), 25)

    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    context = {'data_list': data_list}

    return render(request, 'registration/administrations/transaction/all_transaction.html', context)


@login_required(login_url=settings.LOGIN_URL)
def approval_transaction(request, id):
    if not get_user(request):
        raise Http404
    else:
        data_list = TransactionDepositVerified.objects.using('transaction_slave').raw(
            "select transaction_transactiondepositverified.transaction_deposit_verified_id,"
            "transaction_transactiondeposittransit.transaction_deposit_transit_id,"
            "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_id,"
            "transaction_transactiondepositverified.transaction_deposit_verified_transit_code,"
            "transaction_transactiondepositverified.transaction_deposit_verified_user_related,"
            "transaction_transactiondeposittransit.transaction_deposit_transit_gt_amount,"
            "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_amount,"
            "transaction_transactiondeposittransit.transaction_deposit_transit_type, "
            "transaction_transactiondeposittransit.transaction_deposit_transit_amount, "
            "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_type, "
            "transaction_transactiondepositverified.transaction_deposit_verified_status "
            "from transaction_transactiondepositverified "
            "left join transaction_transactiondeposittimetransit on "
            "transaction_transactiondepositverified.transaction_deposit_verified_transit_code="
            "transaction_transactiondeposittimetransit.transaction_deposit_time_transit_code "
            "left join transaction_transactiondeposittransit on "
            "transaction_transactiondepositverified.transaction_deposit_verified_transit_code="
            "transaction_transactiondeposittransit.transaction_deposit_transit_code "
            "where transaction_transactiondepositverified.transaction_deposit_verified_transit_code=%s", [id])

        if request.method == 'POST':
            transaction = ApprovalForm(request.POST)
            if transaction.is_valid():
                post_save.disconnect(approval_transactions_deposit)
                for data in data_list:
                    data
                query_principal = DepositMemberPrincipal.objects.using('funds_slave').filter(
                    deposit_member_principal_user_related=data.transaction_deposit_verified_user_related
                )
                query_mandatory = DepositMemberMandatory.objects.using('funds_slave').filter(
                    deposit_member_mandatory_user_related=data.transaction_deposit_verified_user_related
                )
                transaction.member_id = data.transaction_deposit_verified_user_related
                transaction.get_choice = transaction.cleaned_data.get("Verifikasi")
                transaction.code_id = id
                transaction.user = get_user(request)
                transaction.first_time = query_principal.values_list(
                    'deposit_member_principal_user_related', flat=True).first()
                transaction.get_current_mandatory_amount = query_mandatory.values_list(
                    'deposit_member_mandatory_amount', flat=True).first()
                transaction.for_mandatory_amount = data.transaction_deposit_transit_gt_amount - 200000 if query_principal.values_list(
                    'deposit_member_principal_payment_principal_status', flat=True).first() is False \
                    else data.transaction_deposit_transit_amount \
                         + transaction.get_current_mandatory_amount

                transaction.for_principal_amount = data.transaction_deposit_transit_gt_amount - \
                    transaction.for_mandatory_amount if query_principal.values_list(
                        'deposit_member_principal_payment_principal_status', flat=True).first() is False \
                    else 0 + query_principal.values_list('deposit_member_principal_payment_principal_amount', flat=True) \
                    .first()

                transaction.left = int(transaction.for_mandatory_amount / 10000)
                transaction.end_date = datetime.now() + relativedelta(months=transaction.left)
                # do loan first
                # transaction.type = 'Credit' if else 'Deposito'
                post_save.send(
                    sender=TransactionDepositVerified, created=None, instance=transaction,
                    dispatch_uid="approval_transactions_deposit")
                messages.success(request, 'Data Berhasil disimpan')
                return redirect('transaction:all-transaction')
        else:
            form = ApprovalForm()
        context = {'data_list': data_list, 'form': form}
        return render(request, 'registration/administrations/transaction/approval.html', context)
