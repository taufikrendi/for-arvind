from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import UpdateView


from utils.forms import ConfirmPasswordForm

from asgiref.sync import sync_to_async
# from silk.profiling.profiler import silk_profile


# Create your views here.
class ConfirmPasswordView(UpdateView):
    form_class = ConfirmPasswordForm
    template_name = 'registration/administrations/utils/confirm_password.html'

    # @silk_profile(name='Password Confirmation')
    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return self.request.get_full_path()