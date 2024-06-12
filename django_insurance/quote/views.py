from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms 
# need to import views in the urls.py of quote

# Create your views here.
# MAKE A VIEW FOR MY FORM 
# IT NEEDS TO TELL DJANGO TO FIND THAT FORM. 
# MAKE A PATH AND A URL. 

def formview():
    form = forms.Contact_Information_Form

    # this method is called when a valid form data has been POSTed. 
    # def form_valid(self, form):
    #     form
    #     return super().form_valid(form)
    #
    
    