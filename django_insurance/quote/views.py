# quote/views.py

from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from quote import models
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from quote.forms import DriverForm
import random 

# need to import views in the urls.py of quote

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
    template_name = "customer.html"

    def get_success_url(self):
        return f"/quote/customer/{self.object.pk}"
    
    # we need to utilize the setup() function in createview. we need to add functionality 
    # to setup to create a quote_id for django to know that this quote is for this customer. 

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:  
        self.quote_id = create_quote_id()
        return super().setup(request, *args, **kwargs)

    # each view has its own context
    # in order to change context in django we need the get_context function 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote_id'] = self.quote_id
        return context
    
    
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
    template_name = "customer.html"

    def get_success_url(self):
        return f"/quote/customer/{self.object.pk}"

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = "My Company"
        context['description'] = "We provide the best services."
        return context

class AboutPageView(TemplateView): 
    template_name = "about.html"

# class DriverView(FormView):
#     template_name = "driver.html"


def driver_form(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        print(f'form valid? : {form.is_valid()}')
        # process form data
    form = DriverForm()
    return render(
        request,
        'driver.html',
        {
            'form': form,
        }
    )

def create_quote_id():
    # Start the string with "d" and "j"
    result = "dj"
    # Append 6 randomly selected numbers from the range 1 to 10
    for _ in range(6):
        result += str(random.randint(1, 10))
    return result