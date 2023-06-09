from django import forms
from django_otp.forms import OTPAuthenticationForm


class AuthenticationForm(OTPAuthenticationForm):
    otp_device = forms.CharField(required=False, widget=forms.HiddenInput)
    otp_challenge = forms.CharField(required=False, widget=forms.HiddenInput)


class SelectCompany(forms.Form):
    select_company = forms.ModelChoiceField(
        queryset=None, required=False, label="Company"
    )

    def __init__(self, *args, **kwargs):
        companies = kwargs.pop("companies")
        super().__init__(*args, **kwargs)

        self.fields["select_company"].queryset = companies.order_by("name")
