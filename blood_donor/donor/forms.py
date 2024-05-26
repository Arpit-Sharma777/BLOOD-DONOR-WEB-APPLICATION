from django import forms
from .models import Donor, BloodRequest, BLOOD_GROUPS
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")

class DonorForm(forms.ModelForm):
    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS)
    phone_number = forms.CharField(validators=[phone_regex])


    class Meta:
        model = Donor
        fields = ['name', 'age', 'weight', 'email', 'blood_group', 'phone_number', 'address', 'city', 'state', 'zip_code']

class BloodRequestForm(forms.ModelForm):
    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS)

    class Meta:
        model = BloodRequest
        fields = ['blood_group', 'location']

