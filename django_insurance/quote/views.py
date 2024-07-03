from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms, models
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# need to import views in the urls.py of quote

# Create your views here.


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
    success_url = "customer/{id}/"
    template_name = "customer.html"


class Customer_UpdateView(UpdateView):
    model = models.Customer
    fields = [
        "first_name",
        "last_name",
        "address",
        "zip_code",
        "telephone_number",
        "email_address",
        "date_of_birth",
        "home_ownership",
    ]
    template_name_suffix = "_update_form"
    success_url = "customer/{pk}/"
    template_name = "customer.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["test"] = "test info"
        return context
