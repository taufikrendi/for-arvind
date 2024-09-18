from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect

from account.models import AccountMemberVerifyStatus


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(username=uid)
    try:
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            AccountMemberVerifyStatus.objects.filter(account_member_verify_status_user_related=uid).update(
                account_member_verify_status_email=True,
                account_member_verify_status_email_filled_date=datetime.now()
            )
            messages.success(request, 'Selamat Account Anda Telah Aktif')
            # Return to Login Website
            return redirect('/')
        else:
            messages.error(request, 'Link Telah Expired')
            return render(request, 'registration/front/used_link.html')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return user
