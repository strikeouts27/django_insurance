from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms, models
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# need to import views in the urls.py of quote

# Create your views here.
class ContactFormView(FormView):
    template_name = "customer.html"
    form_class = forms.Customer_Form
    # need to build success_url 
    success_url = "customer"

class Customer_CreateView(CreateView):
    model = models.Customer
    fields = [
        "first_name",
        "last_name",
        "address",
        "telephone_number",
        "zip_code",
        "email_address",
        "date_of_birth",
        "home_ownership",
    ]
    success_url = "customer/{pk}/"
    template_name = "customer.html"

class Customer_UpdateView(UpdateView): 
    model = models.Customer
    fields = [
        "first_name",
        "last_name",
        "address",
        "telephone_number",
        "zip_code",
        "email_address",
        "date_of_birth",
        "home_ownership",
    ]
    template_name_suffix = "_update_form"
    success_url = "customer/{pk}/"
    template_name = "customer.html"
