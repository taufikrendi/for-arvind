from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.utils import timezone


from utils.enums_factory import LoanType, Approval


class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', help_text='Confirm password',
                                       required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('confirm_password', )

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password Tidak Cocok')

    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user


class ApprovalForm(forms.Form):
    Verifikasi = forms.ChoiceField(
        choices=[(tag, tag.value) for tag in Approval], label='Verifikasi', required=True,
        error_messages={'required': "Pilih Salah Satu"}, help_text='Pilih Salah Satu',
        widget=forms.RadioSelect()
    )

    def clean(self):
        super(ApprovalForm, self).clean()

        Verifikasi = self.cleaned_data.get("Verifikasi")
        if not Verifikasi: self._errors['Verifikasi'] = self.error_class(['Harus Dipilih!'])


class LoanSelected(forms.Form):
    Tipe = forms.ChoiceField(
        choices=[(tag, tag.value) for tag in LoanType], label='Tipe Pinjaman', required=True,
        help_text='Pilih Salah Satu',)

    def clean(self):
        super(LoanSelected, self).clean()
    
        Tipe = self.cleaned_data.get("Tipe")
        if not Tipe: self._errors['Tipe'] = self.error_class(['Harus dipilih'])



