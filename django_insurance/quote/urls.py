from django.urls import path
from django.views.generic import TemplateView
from quote.views import AboutPageView, Customer_CreateView, Customer_UpdateView, HomePageView, driver_form


urlpatterns = [
    path("quote/customer/create/", Customer_CreateView.as_view(), name='customer'),
    path("quote/customer/<int:pk>", Customer_UpdateView.as_view(),),
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about"),
    path("driver/", driver_form, name="driver"),
]