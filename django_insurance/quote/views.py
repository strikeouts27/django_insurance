# quote/views.py

from typing import Any
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from quote.forms import DriverForm, Customer_Form
from quote import models
import random

# need to import views in the urls.py of quote

class Customer_CreateView(CreateView):
    quote_id: str = None
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
        "quote_id"
    ]
    template_name = "customer.html"

    def get_success_url(self):
        return "/driver"

    # we need to utilize the setup() function in createview. we need to add functionality 
    # to setup to create a quote_id for django to know that this quote is for this customer. 
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('quote_id', self.quote_id, max_age=3600)
        return response

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:  
        current_quote_id = request.COOKIES.get('quote_id', '')
        print(f'current_quote_id: {current_quote_id}')
        if not self.quote_id and not current_quote_id:
            self.quote_id = create_quote_id()
            print(f'setting up quote id: {self.quote_id}')
        else:
            print(f'setting to current_quote_id: {current_quote_id}')
            self.quote_id = current_quote_id
        return super().setup(request, *args, **kwargs)

    # each view has its own context
    # in order to change context in django we need the get_context function 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote_id'] = self.quote_id
        context['title'] = "Customer Page"
        return context


# class Customer_UpdateView(UpdateView):
#     model = models.Customer
#     fields = [
#         "first_name",
#         "last_name",
#         "address",
#         "zip_code",
#         "telephone_number",
#         "email_address",
#         "date_of_birth",
#         "home_ownership",
#     ]
#     template_name_suffix = "_update_form"
#     template_name = "customer.html"

#     def get_success_url(self):
#         return f"/driver"

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home Page"
        context['description'] = "We provide the best services."
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

# class DriverView(FormView):
#     template_name = "driver.html"


def driver_form(request):
    quote_id = request.COOKIES.get('quote_id')
    if request.method == 'POST':
        form = DriverForm(request.POST)
        print(f'form valid? : {form.is_valid()}')
        if form.is_valid():
            # form and model are not in sync. NEEDS WORK!
            print(form.cleaned_data['Usage_Type'])
            print(f'this is the quote id from the http request: {form.cleaned_data['quote_id']}')
            # process form data
    form = DriverForm()
    return render(
        request,
        'driver.html',
        {
            'form': form,
            'title': 'Driver Page',
            'quote_id': quote_id,
        }
    )

def create_quote_id():
    # Start the string with "d" and "j"
    result = "dj"
    # Append 6 randomly selected numbers from the range 1 to 10
    for _ in range(6):
        result += str(random.randint(1, 10))
    return result
