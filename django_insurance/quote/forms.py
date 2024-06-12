from django import forms 

class Customer_Form(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

# THIS BELONGS IN FORMS.PY
class Contact_Information_Form(django_forms.Form):
    template_name = "customer.html"
    form_class = forms.Customer_Form
