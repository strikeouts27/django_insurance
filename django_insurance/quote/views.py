# quote/views.py

from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from quote.forms import DriverForm, VehicleForm
from quote import models
from django.views.generic.list import ListView
import random
from django.core import validators
from django.forms import CharField 


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
        "home_ownership"
    ]
    template_name = "customer.html"

    def form_valid(self, form):
        form.instance.quote_id = self.quote_id
        return super().form_valid(form)

    def get_success_url(self):
        return f"/driver/list/{self.quote_id}"

    # we need to utilize the setup() function in createview. we need to add functionality 
    # to setup to create a quote_id for django to know that this quote is for this customer. 
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:  
        current_quote_id = request.COOKIES.get('quote_id', '')
        if current_quote_id:
            self.quote_id = current_quote_id
            print(f'setting up quote id: {self.quote_id}')
        else:
            self.quote_id = create_quote_id()
        return super().setup(request, *args, **kwargs)

    # each view has its own context
    # in order to change context in django we need the get_context function 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote_id'] = self.quote_id
        context['title'] = "Customer Page"
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('quote_id', self.quote_id, max_age=3600)
        return response


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home Page"
        context['description'] = "We provide the best services."
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"


class DriverListView(ListView):
    template_name = 'driver-list.html'
    model = models.Driver
    # object_list

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.quote_id = kwargs['quote_id']
        print(f"Quote is: {self.quote_id}")
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['quote_id'] = self.quote_id
        print(f"context is: {context}")
        driver_list = models.Driver.objects.filter(quote_id=self.quote_id)
        context['driver_list'] = driver_list
        print(f"context is: {context}")
        return context


def vehicle_form_view(request):
    quote_id = request.COOKIES.get('quote_id')
    # TODO handle post request to validate and save data.
    form = VehicleForm()
    return render(
        request,
        'vehicles.html',
        {
            'form': form,
            'title': 'Vehicle',
            'quote_id': quote_id,
        }
    )


def driver_form(request, quote_id):
    # TODO should not allow access to this page without a quote id
    # in order to maintain data integrity
    # quote_id = request.COOKIES.get('quote_id')
    print(f"Quote id is: {quote_id}")
    print(f"request method: {request}")

    if request.method == 'POST':
        form = DriverForm(request.POST)
        print(f'form valid? : {form.is_valid()}')
        breakpoint()
        if form.is_valid():
            form.quote_id = quote_id
            breakpoint()
            print('saving valid driver record')
            form.save()
           
            return redirect(f'/driver/list/{quote_id}')
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
    result = "dj"
    for _ in range(6):
        result += str(random.randint(1, 10))
    return result