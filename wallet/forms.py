from django import forms

def large_amount_validator(amount):
    if int(amount)>10000:
        raise forms.ValidationError('You cannot add more than 10000 in one transaction')

class AddMoneyForm(forms.Form):
    amount=forms.DecimalField(decimal_places=2,max_digits=20,widget=forms.TextInput(
        attrs={'placeholder': 'Eg: 2,000,000.00'}),validators=[large_amount_validator])
    