from django import forms


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
    telephone_number = forms.IntegerField(
        required=True, label="What is your phone number?"
    )
    email = forms.EmailField(
        max_length=50, required=False, label="What is your email address?"
    )
    date_of_birth = forms.DateField(required=True, label="What is your date of birth?")
    home_ownership = forms.CharField(label="Do you own or rent your home?")


class Vehicle_Form(forms.Form):
    Vehicle_Identification_Number = forms.IntegerField(
        required=True,
        label="What is the vehicle identification number for your vehicle?",
    )
    Annual_Mileage = forms.IntegerField(
        required=True, label="How many miles do you drive each year?"
    )


class DriverForm(forms.Form):

    Usage_Type = forms.CharField(
        required=True,
        label="Will this vehicle be used for work, school, pleasure, or business?",
    )
    Driver_First_Name = forms.CharField(
        required=True, label="What is your drivers first name?"
    )
    Driver_Last_Name = forms.CharField(
        required=True, label="What is your drivers last name?"
    )
    Driver_Relation = forms.CharField(
        required=True, label="What is the relationship does this driver have to you?"
    )
    US_State = forms.CharField(
        required=True, label="In what US state do you have your license?"
    )
    Drivers_License_Number = forms.IntegerField(
        required=True, label="What is your drivers license number?"
    )
    Drivers_License_Status = forms.CharField(
        required=True, label="What is your current status of your drivers license?"
    )
