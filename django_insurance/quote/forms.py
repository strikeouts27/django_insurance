from django import forms 

class Customer_Form(forms.Form):
    first_name = forms.CharField(max_length=20, label="What is your first name?", required=True)
    last_name = forms.CharField(max_length=20, label='What is your last name?', required=True)
    address = forms.CharField(max_length=50, label="What is your address?", required=True)
    zip_code = forms.IntegerField(label="What is your zip code?")
    # dashes between the number 
    telephone_number = forms.IntegerField(required=True, label='What is your phone number?')
    email = forms.EmailField(max_length= 50, required=False, label='What is your email address?')
    date_of_birth = forms.DateField(required=True, label='What is your date of birth?')
    home_ownership = forms.CharField(label="Do you own or rent your home?")






