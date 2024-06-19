from django import forms 

class Customer_Form(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=20, label="What is your address?")
