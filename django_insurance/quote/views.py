from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms 
from django.views.generic.edit import FormView

# need to import views in the urls.py of quote

# Create your views here.
class ContactFormView(FormView):
    template_name = "customer.html"
    form_class = forms.Customer_Form
    # need to build success_url 
    success_url = "/thanks/"



    # this method is called when a valid form data has been POSTed. 
    # def form_valid(self, form):
    #     form
    #     return super().form_valid(form)
    #
    
    