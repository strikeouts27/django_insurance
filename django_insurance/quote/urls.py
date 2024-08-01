from django.urls import path
from quote.views import (
    AboutPageView,
    Customer_CreateView,
    HomePageView,
    driver_form,
    vehicle_form_view
)

urlpatterns = [
    path("quote/customer/create/", Customer_CreateView.as_view(), name='customer'),
    path("about/", AboutPageView.as_view(), name="about"),
    path("driver/", driver_form, name="driver"),
    path("vehicle/", vehicle_form_view, name="vehicle"),
    path("", HomePageView.as_view(), name='home'),
]
