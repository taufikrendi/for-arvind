import time as time_

from datetime import datetime, timezone

from functools import wraps

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import redirect
from django.utils import timezone

from account.models import AccountBankUsers, AccountProfile
from account.models import AccountPasswordExpired
from utils.validators import get_user


user_login_required = user_passes_test(lambda user: user.is_active, login_url='/accounts/login/')


# The way to use this decorator is:
# @group_required('admin', 'membership')
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url=settings.LOGIN_URL)


# The way to use this decorator is:
# @active_user_required
def active_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func


# The way to use this decorator is:
# @anonymous_required
def anonymous_required(function=None, redirect_url=None):
   if not redirect_url:
       redirect_url = HttpResponseRedirect('account:login')

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous == True,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


# The way to use this decorator is:
# @ajax_required
def ajax_required(f):

   def wrap(request, *args, **kwargs):
       if not request.is_ajax():
           return HttpResponseBadRequest()
       return f(request, *args, **kwargs)

   wrap.__doc__=f.__doc__
   wrap.__name__=f.__name__
   return wrap


# The way to use this decorator is:
# @superuser_only
def superuser_only(function):
   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied
       return function(request, *args, **kwargs)
   return _inner


# The way to use this decorator is:
# @timeit
def timeit(method):
   def timed(*args, **kw):
       ts = time_.time()
       result = method(*args, **kw)
       te = time_.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result

   return timed


# The way to use this decorator is:
# @confirm_password
# https://simpleisbetterthancomplex.com/tutorial/2016/08/15/how-to-create-a-password-confirmation-view.html
def confirm_password(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        import datetime
        last_login = request.user.last_login
        timespan = last_login + datetime.timedelta(minutes=15)
        if timezone.now() > timespan:
            from utils.views import ConfirmPasswordView
            return ConfirmPasswordView.as_view()(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# The way to use this decorator is:
# @profile_not_complete
def profile_not_complete(function):
    def wrapper(request, *args, **kwargs):
        check = AccountBankUsers.objects.filter(
            account_bank_user_related_to_user=get_user(request))\
            .values_list('account_bank_user_number', flat=True).latest('account_bank_user_number')
        check_two = AccountProfile.objects.filter(account_profile_user_related=get_user(request))\
            .values_list('account_profile_identification_number', flat=True).first()
        if not check:
            messages.error(request, 'Anda Belum Mengisi Akun Bank!')
            return redirect('account:detail-account')
        elif not check_two:
            messages.error(request, 'Anda Belum Mengisi Profil Anda')
            return redirect('account:detail-account')
        else:
            return function(request, *args, **kwargs)
    return wrapper


# The way to use this decorator is:
# @password_force_change
def password_force_change(function):
    def wrapper(request, *args, **kwargs):
        check = AccountPasswordExpired.objects.filter(account_password_expired_user_related=request.user) \
            .values_list('account_password_expired_last_updated', flat=True).latest('account_password_expired_last_updated')
        count = datetime.now().date() - check.date()
        if count.days >= 30:
            messages.error(request, 'Anda Harus Mengganti Password Anda!')
            return redirect('account:change-password')
        else:
            return function(request, *args, **kwargs)
    return wrapper