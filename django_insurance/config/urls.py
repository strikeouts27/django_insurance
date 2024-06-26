"""
URL configuration for web_scrap_cloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py -> django_project url
from django.contrib import admin
from django.urls import path, include
from django_insurance.quote import views as quote_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quote/customer", quote_views.ContactFormView.as_view()),
    path("quote/customer/create/", quote_views.Customer_CreateView.as_view()),
    path("quote/customer/<int:pk>", quote_views.Customer_UpdateView.as_view()),
]
