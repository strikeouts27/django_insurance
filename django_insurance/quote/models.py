from django.db import models
from quote import constants

# makemigrations and migrate from manage.py
# Create your models here.

# Tie everything with Quote ID


# customer model
class Customer(models.Model):
    # columns would be the variables
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(blank=True, max_length=10)

    apt_number = models.CharField(blank=True, max_length=10)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    zip_code = models.CharField(default=00000, max_length=10)
    telephone_number = models.IntegerField()
    email_address = models.CharField(max_length=50)
    quote_id = models.CharField(max_length=8, blank=True)
    home_ownership_options = (("OWN", "Owns_Property"), ("RENT", "Rents_Property"))
    home_ownership = models.CharField(max_length=50, choices=home_ownership_options)


# credit
# vehicle model
#
class Vehicle(models.Model):
    Vehicle_Identification_Number = models.CharField(max_length=30)
    # Enumerate Technique The first item in the tuple is what will be listed in the database.
    # The second item in the tuple is what will display for the user.
    Usage_Type_Options = (
        ("PLEASURE", "Pleasure Vehicle"),
        ("WORK", "Work/School"),
        ("BUSINESS", "Business"),
        ("COMMERCIAL", "Commercial"),
    )
    # Note: Use for ride sharing ideally should be like a check box 
    Used_For_Ride_Sharing = models.CharField(max_length = 10, blank=True)
    Usage_Type = models.CharField(choices=Usage_Type_Options, max_length=11, blank=True)
     
    Annual_Mileage_Options = (
        ("0 - 3,999", "0 - 3,999"), 
        ("4,000 - 5,999","4,000 - 5,999"),
        ("6,000 - 7,999", "6,000 - 7,999"), 
        ("8,000 - 9,999", "8,000 - 9,999"), 
        ("10,000 - 11,999", "10,000 - 11,999"), 
        ("12,000 - 13,999", "12,000 - 13,999"), 
        ("14,000 - 15,999", "14,000 - 15,999"), 
        ("16,000 - 17,999", "16,000 - 17,999"), 
        ("18,000 - 19,999", "18,000 - 19,999"), 
        ("20,000 OR MORE", "20,000 or more"), 
    )
    
    Annual_Mileage = models.CharField(choices=Annual_Mileage_Options, max_length=15)
    Year = models.IntegerField()
    Make = models.CharField(max_length=30)
    quote_id = models.CharField(max_length=8, blank=True)
    Model = models.CharField(max_length=30)
    
    Ownership_Options = (
        ("FINANCE", "Finance"),
        ("OWN", "Own"),  
        ("LEASE", "Lease"), 
    )
    
    Vehicle_Ownership = models.CharField(choices=Ownership_Options, max_length=11)
    
    Vehicle_Ownership_Timeframe_Options = (
        ("LESS THAN 1 MONTH", "Less than 1 month"), 
        ("1 TO 6 MONTHS", "1 to 6 months"), 
        ("6 MONTHS TO 1 YEAR", "6 months to 1 year"), 
        ("1 YEAR TO 3 YEARS", "1 year to 3 years"), 
        ("3 YEARS TO 5 YEARS", "3 years to 5 years"), 
        ("5 YEARS OR MORE", "5 years or more"),
    )
    
    Vehicle_Ownership_Timeframe = models.CharField(max_length=15)


class Driver(models.Model):
    driver_first_name = models.CharField(max_length=50)
    driver_last_name = models.CharField(max_length=50)
    driver_relation = models.CharField(max_length=16, choices=constants.DRIVER_RELATION_OPTIONS, default="SELF")
    quote_id = models.CharField(max_length=8, blank=True)
    drivers_license_state = models.CharField(choices=constants.STATE_OPTIONS, max_length=30)
    drivers_license_number = models.CharField(max_length=30)
    drivers_license_status = models.CharField(choices=constants.DRIVERS_LICENSE_STATUS, max_length=50)
    gender = models.CharField(choices=constants.GENDER_OPTIONS, max_length=30)
    date_of_issuance = models.DateField()
    job_status = models.CharField(max_length=50, choices=constants.JOB_STATUS_OPTIONS)
    education = models.CharField(choices=constants.EDUCATION_OPTIONS, max_length=35)
    affilation_options = (("DFW_PYTHONEERS", "Dfw_Pythoneers"),
                          ("PY_TEXAS", "Py_Texas"),)
    affilation = affilation_options


# many to many relationship QUOTE to PRODUCT
# state of texas requirements (LIABLITY,PIP,)
class Product(models.Model):
    product_type_options = (
        ("LIABILITY", "Liability"),
        ("RECCOMENDED_COVERAGE", "Reccomended Coverage"),
        ("CUSTOM", "Custom"),
    )
    coverage_options = (("FULL_COVERAGE", "Full Coverage"),)


# adding products to customers
# if not defined in a table before than you must use quotes for the model not defined.
# since everything is already defined already we do not need to worry about that.
class Quote(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Reference_Number = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=7, decimal_places=2)

# url for vehcile we want to build a vehicle or for this quote 
