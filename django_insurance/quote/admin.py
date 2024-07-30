from django.contrib import admin
from quote.models import Customer, Driver, Product, Quote, Vehicle
# Register your models here.
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Vehicle)
