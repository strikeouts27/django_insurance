from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms 
# need to import views in the urls.py of quote

# Create your views here.
class Contact_Information_Form(django_forms.Form):

    template_name = "customer.html"
    form_class = forms.Customer_Form 

    # this method is called when a valid form data has been POSTed. 
    # def form_valid(self, form):
    #     form
    #     return super().form_valid(form)
    #
    
    