from django.db import models

#makemigrations and migrate from manage.py 
# Create your models here.

# Tie everything with Quote ID 

# customer model
class Customer(models.Model):
    # columns would be the variables 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone_number = models.IntegerField()
    zip_code = models.CharField()
    email_address = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    home_ownership_options = (("OWN", "Owns_Property"), ("RENT", "Rents_Property"))
    home_ownership = models.CharField(max_length=50, choices=home_ownership_options)
# credit 
# vehicle model
#
class Vehicle(models.Model): 
    Vehicle_Identification_Number = models.CharField(max_length=17)
    # Enumerate Technique The first item in the tuple is what will be listed in the database.
    # The second item in the tuple is what will display for the user. 
    Usage_Type_Options =( 
        ("PLEASURE", "Pleasure Vehicle"),
        ("WORK", "Work/School"),
        ("BUSINESS", "Business"),
        ("COMMERCIAL", "Commercial"),
    )
    Usage_Type = models.CharField(choices=Usage_Type_Options, max_length=11, blank=True)
    Annual_Mileage = models.IntegerField()
    Year = models.IntegerField()
    Make = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)

    
class Drivers(models.Model): 
    Drivers_License = models.CharField(max_length=25)
    Drivers_License_State = models.TextField(max_length=25)
    gender_options = (
        ("MALE", "Male"), 
        ("WOMAN", "Woman"),
        ("NONBINARY", "NonBinary"),
    )
    gender = (models.CharField(gender_options,  max_length=1))
    driving_experience = (models.IntegerField())
    job_status_options = (
        ("FULL_TIME_EMPLOYED", "Full Time Employed"),
        ("PART_TIME_EMPLOYED", "Part Time Employed"), 
    )

# many to many relationship QUOTE to PRODUCT 
# state of texas requirements (LIABLITY,PIP,)
class Product(models.Model):
    product_type_options = (
        ("LIABILITY", "Liability"),
        ("RECCOMENDED_COVERAGE", "Reccomended Coverage"),
        ("CUSTOM", "Custom"), 
    )
    coverage_options = (
        ("FULL_COVERAGE", "Full Coverage"),
    )

# adding products to customers 
# if not defined in a table before than you must use quotes for the model not defined. 
# since everything is already defined already we do not need to worry about that. 
class Quote(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Drivers = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    Reference_Number = models.CharField(max_length=25)
    Price = models.DecimalField(max_digits=7, decimal_places= 2)


