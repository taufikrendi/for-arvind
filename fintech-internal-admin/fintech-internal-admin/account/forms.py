from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    email = forms.CharField(
        label='E-mail', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        super(LoginForm, self).clean()

        email = self.cleaned_data.get("email")
        if not email: self._errors['email'] = self.error_class(['Harus diisi'])

        password = self.cleaned_data.get("password")
        if not password: self._errors['password'] = self.error_class(['Harus diisi'])