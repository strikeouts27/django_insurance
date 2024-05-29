# quote/urls.py -> app urls 
from django.urls import path 
from . import views

urlpatterns = [
    path("customer", views.Contact_Information_Form),
    
]
