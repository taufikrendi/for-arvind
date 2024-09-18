import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from account.forms import LoginForm
from account.models import AccountMemberVerifyStatus
from account.signals import approval_member
from utils.decorators import group_required, password_force_change, confirm_password
from utils.forms import ApprovalForm
from utils.validators import get_user
from django.http import Http404, HttpResponse


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_check = form.save(commit=False)
            login_check.email = form.cleaned_data.get("email")
            login_check.password = form.cleaned_data.get("password")
            user = authenticate(request, username=login_check.email, password=login_check.password)
            user_active = User.objects.filter(username=login_check.email, is_active=True)
            next = request.GET.get('next')
            if user and user_active and next:
                login(request, user)
                return redirect(next)
            elif user and user_active and next is None:
                login(request, user)
                return redirect('account:dashboard')
            else:
                messages.error(request, 'Login Gagal, Username & Password Tidak Sesuai')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


# with g-recaptcha
# response = {}
# data = request.POST
# captcha_rs = data.get('g-recaptcha-response')
# url = "https://www.google.com/recaptcha/api/siteverify"
# params = {
#     'secret': settings.RECAPTCHA_SECRET_KEY,
#     'response': captcha_rs,
#     'remoteip': get_client_ip(request)
# }
# verify_rs = requests.get(url, params=params, loan=True)
# verify_rs = verify_rs.json()
# response["status"] = verify_rs.get("success", False)
# response['message'] = verify_rs.get('error-codes', None) or "Unspecified error."


@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
def user_logout(request):
    logout(request)
    return render(request, template_name='registration/logged_out.html')


@csrf_protect
@password_force_change
@confirm_password
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, template_name='registration/administrations/dashboard.html')


@group_required("Operator")
@csrf_protect
@password_force_change
@confirm_password
@login_required(login_url=settings.LOGIN_URL)
def all_member(request):
    if not get_user(request):
        raise Http404
    data = User.objects.filter(Q(is_staff=False) & Q(groups=1)) \
        .extra(
        select={'account_member_verify_status_revision_profile': 'account_accountmemberverifystatus.account_member_verify_status_revision_profile',
                'account_member_verify_status_id': 'account_accountmemberverifystatus.account_member_verify_status_id',
                'account_member_verify_status_email': 'account_accountmemberverifystatus.account_member_verify_status_email',
                'account_profile_phone_number': 'account_accountprofile.account_profile_phone_number',
                'account_member_verify_status_bank': 'account_accountmemberverifystatus.account_member_verify_status_bank',
                'account_member_verify_status_legal_doc_sign': 'account_accountmemberverifystatus.account_member_verify_status_legal_doc_sign',
                'account_member_verify_status_profile_close_to_update': 'account_accountmemberverifystatus.account_member_verify_status_profile_close_to_update',
                'account_member_verify_status_revision_profile_last_date': 'account_accountmemberverifystatus.account_member_verify_status_revision_profile_last_date'},
        tables=['account_accountmemberverifystatus', 'account_accountprofile'],
        where=['account_accountmemberverifystatus.account_member_verify_status_user_related=auth_user.username',
               'account_accountprofile.account_profile_user_related=auth_user.username']
    ).order_by('-date_joined')

    search = request.POST.get('search')
    active = request.POST.get('release')
    completed = request.POST.get('completed')
    bank_accounts = request.POST.get('bank_accounts')
    email = request.POST.get('email')

    if search:
        data = data.filter(Q(email__contains=search))
    elif active:
        if AccountMemberVerifyStatus.objects.using('default_slave').filter(
            account_member_verify_status_user_related=active,
            account_member_verify_status_email=True
        ):
            data.using('default').filter(Q(username=active)).update(is_active=True)
            messages.success(request, 'Berhasil Membuka Blokir Anggota')
        else:
            messages.error(request, 'Calon Anggota Belum Verifikasi E-MAIL!')
    else:
        data.using('default_slave')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 25)

    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    context = {'data_list': data_list}

    return render(request, 'registration/administrations/account/all_member.html', context)


@group_required("Operator")
@password_force_change
@confirm_password
@login_required(login_url=settings.LOGIN_URL)
def approval_member(request, id):
    data = AccountMemberVerifyStatus.objects.using('default_slave').filter(
        account_member_verify_status_id=id).extra(
        select={'first_name': 'auth_user.first_name',
                'account_profile_phone_number':'account_accountprofile.account_profile_phone_number',
                'account_profile_created_date': 'account_accountprofile.account_profile_created_date',
                'account_profile_identification_number': 'account_accountprofile.account_profile_identification_number',
                'account_profile_tax_identification_number': 'account_accountprofile.account_profile_tax_identification_number',
                'account_profile_address': 'account_accountprofile.account_profile_address',
                'account_profile_address_prov': 'account_accountprofile.account_profile_address_prov',
                'account_profile_address_district': 'account_accountprofile.account_profile_address_district',
                'account_profile_address_sub_district': 'account_accountprofile.account_profile_address_sub_district',
                'account_profile_eidentity': 'account_accountprofile.account_profile_eidentity',
                'account_profile_enpwp': 'account_accountprofile.account_profile_enpwp',
                'account_profile_selfie': 'account_accountprofile.account_profile_selfie',
                'account_profile_selfie_eidentity': 'account_accountprofile.account_profile_selfie_eidentity',
                'bank_name': 'utils_banks.bank_name',
                'account_bank_user_number':'account_accountbankusers.account_bank_user_number',
                'account_bank_user_name': 'account_accountbankusers.account_bank_user_name'},
        tables=['account_accountprofile', 'account_accountbankusers', 'utils_banks', 'auth_user',
                'utils_province', 'utils_district', 'utils_subdistrict'],
        where=['account_accountmemberverifystatus.account_member_verify_status_user_related'
               '=account_accountprofile.account_profile_user_related',
               'account_accountbankusers.account_bank_user_related_to_user'
               '=account_accountmemberverifystatus.account_member_verify_status_user_related',
               'utils_banks.bank_code=account_accountbankusers.account_bank_user_related_to_bank',
               'account_accountmemberverifystatus.account_member_verify_status_user_related=auth_user.username',]
    )
    if request.method == 'POST':
        approval = ApprovalForm(request.POST)
        if approval.is_valid():
            post_save.disconnect(approval_member)
            approval.user = get_user(request)
            approval.get_choice = approval.cleaned_data.get("Verifikasi")
            approval.get_member = data.values_list('account_member_verify_status_user_related', flat=True).first()
            approval.get_current_revision = data.values_list('account_member_verify_status_revision_profile', flat=True).first()
            approval.revision = approval.get_current_revision + int(1)
            # return HttpResponse(int(float(datetime.datetime.now().timestamp()) * 100))
            post_save.send(
                sender=AccountMemberVerifyStatus, created=None, instance=approval,
                dispatch_uid="approval_member")
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('account:all-member')
    else:
        form = ApprovalForm()
    context = {'data_list': data, 'form': form}
    return render(request, 'registration/administrations/account/approval.html', context)