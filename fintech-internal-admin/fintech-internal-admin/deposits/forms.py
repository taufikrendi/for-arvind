from django import forms

from deposits.models import DepositProductMaster
from utils.enums_factory import Fluctuate


class DepositProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Nama Produk Deposito', label_suffix=" : ", required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Deposito Khusus Motor'}),
        help_text="Nama Produk Deposito", error_messages={'required': "Harus Diisi"})
    revenue = forms.DecimalField(
        label='Revenue Share', label_suffix=" : ", min_value=1, max_value=100, max_digits=6,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}), decimal_places=4, required=True,
        help_text="Nilai dari 1 s/d 100 dengan 4 digit dibelakang koma",
        error_messages={'required': "Harus Diisi"})
    minimum_amount = forms.DecimalField(
        label='Nilai Minimum Deposito', label_suffix=" : ", min_value=1, max_value=999999999999, max_digits=30,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}), decimal_places=12, required=True,
        help_text="Berikan Nilai Minimum Deposito Rp. 1.000.000",
        error_messages={'required': "Harus Diisi"})
    type = forms.ChoiceField(
        label='Tipe Bagi Hasil', label_suffix=" : ", required=True,
        choices=[(tag, tag.value) for tag in Fluctuate],
        error_messages={'required': "Harus Di Pilih"}, help_text='Pilih Tipe Bagi Hasil',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='Deskripsi', label_suffix=" : ", required=True, max_length=500, widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Deposito Khusus Kendaraan Bermotor'}),
        help_text="Deskripsi Produk Deposito", error_messages={'required': "Harus Diisi"})

    class Meta:
        model = DepositProductMaster
        fields = ('name', 'revenue', 'minimum_amount', 'type', 'description')

    def clean(self):
        super(DepositProductForm, self).clean()

        name = self.cleaned_data.get("name")
        if not name: self._errors['name'] = self.error_class(['Harus diisi'])

        revenue = self.cleaned_data.get("revenue")
        if not revenue: self._errors['revenue'] = self.error_class(['Harus diisi'])

        minimum_amount = self.cleaned_data.get("minimum_amount")
        if not minimum_amount: self._errors['minimum_amount'] = self.error_class(['Harus diisi'])
        if minimum_amount < 999999: self._errors['minimum_amount'] = self.error_class(
            ['Nilai Kurang Dari Rp. 1.000.000'])

        type = self.cleaned_data.get("type")
        if not type: self._errors['type'] = self.error_class(['Harus dipilih'])

        description = self.cleaned_data.get("description")
        if not description: self._errors['description'] = self.error_class(['Harus diisi'])