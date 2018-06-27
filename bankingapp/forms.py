from django import forms
from bankingapp.models import FundsTransfer, UtilityPayment

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)


class FundsTransferForm(forms.ModelForm):
    #transferdesc = forms.CharField(max_length=200, help_text="Select Transaction Description")
    #transferaccount = forms.CharField(max_length=10, help_text="Enter Account Number")
    #transferamount = forms.IntegerField(help_text="Enter amount to transfer")
    #recipient_first_name = forms.CharField(max_length=100, help_text="Enter Recipient First Name")
    #recipient_sec_name = forms.CharField(max_length=100, help_text="Enter Recipient Second Name")
    recipient_first_name = forms.ModelChoiceField(queryset=None, empty_label="Enter recipient first name")
    recipient_sec_name = forms.ModelChoiceField(queryset=None, empty_label="Enter recipient second name")
    transferaccount = forms.ModelChoiceField(queryset=None, empty_label="Enter transfer account")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient_first_name'].queryset=FundsTransfer.objects.filter(transferAccount__accountID__first_name="")
        self.fields['recipient_sec_name'].queryset=FundsTransfer.objects.filter(transferAccount__accountID__last_name="")
        self.fields['transferaccount'].queryset=FundsTransfer.objects.filter(transferAccount__accountNumber="")


    # Providing an association between the model form and a model

    class Meta:
        model = FundsTransfer
        fields = ('transferAmount', 'transferDescription')
