# django_insurance/quote/urls.py

from django.urls import path

from quote.views import (
    AboutPageView,
    HomePageView,
    DriverListView,
    customer_form_view, 
    driver_form,
    vehicle_form_view,
)

urlpatterns = [
    path("quote/customer/create/", customer_form_view, name="customer"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("driver/list/<str:quote_id>", DriverListView.as_view(), name="driver_list"),
    path("driver/<str:quote_id>", driver_form, name="driver"),
    path("vehicle/", vehicle_form_view, name="vehicle"),
    path("", HomePageView.as_view(), name="home"),
]
