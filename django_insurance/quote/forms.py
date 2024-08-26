from django import forms
from quote.models import Driver, Vehicle
from django.forms import CharField
from django.core.exceptions import ValidationError


def validate_phone_numbers(input):
    telephone_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for iteration in input:
        if iteration in telephone_numbers:
            continue
        else:
            raise ValidationError("Please input a number from 0 to 9")


class Customer_Form(forms.Form):
    first_name = forms.CharField(
        max_length=20, label="What is your first name?", required=True
    )
    middle_name = forms.CharField(
        max_length=20, label="What is your middle name?"
    )
    last_name = forms.CharField(
        max_length=20, label="What is your last name?", required=True
    )
    suffix = forms.CharField(
        max_length=5, label="If you have a suffix in your name what is it?", required=False
    )
    address = forms.CharField( 
        max_length=50, label="What is your address?", required=True
    )
    zip_code = forms.IntegerField(label="What is your zip code?")
    # dashes between the number
    
    phone_number = forms.CharField(
        validators=[validate_phone_numbers], max_length=10, label="What is your phone number?"
        )
    
    email = forms.EmailField(
        max_length=50, required=False, label="What is your email address?"
    )
    date_of_birth = forms.DateField(required=True, label="What is your date of birth?")
    home_ownership = forms.CharField(label="Do you own or rent your home?")


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "Vehicle_Identification_Number",
            "Usage_Type",
            "Year",
            "Make",
            "Model",
        ]

    quote_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            "driver_first_name",
            "driver_last_name",
            "driver_relation",
            "drivers_license_number",
            "drivers_license_status",
            'drivers_license_state',
            "date_of_issuance",
            "job_status",
            "gender",
            "education",
        ]
        widgets = {
            'date_of_issuance': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    quote_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
