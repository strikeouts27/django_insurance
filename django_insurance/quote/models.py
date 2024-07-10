from django.db import models
from django.views.generic import TemplateView

# makemigrations and migrate from manage.py
# Create your models here.

# Tie everything with Quote ID


# customer model
class Customer(models.Model):
    # columns would be the variables
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(blank=True)
    apt_number = models.CharField(blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    zip_code = models.CharField(default=00000)
    telephone_number = models.IntegerField()
    email_address = models.CharField(max_length=50)
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
     
    # Updated on 7/8/2024
    # Note - reason for update was for better form in the model, therefore the highest option (for now) is 20,000 or more    
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
    
    Annual_Mileage = models.CharField(choices=Annual_Mileage_Options)
    Year = models.IntegerField(max_length=4)
    Make = models.CharField(max_length=30)
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
    
    Vehicle_Ownership_Timeframe = models.CharField()


class Drivers(models.Model):

    Driver_First_Name = models.CharField(max_length=50)
    Driver_Last_Name = models.CharField(max_length=50)
    driver_relation_options = (
        (
            ("SELF, Self"),
            ("GRANDFATHER", "Grandfather"),
            ("GRANDMOTHER", "Grandmother"),
            ("SPOUSE", "Spouse"),
            ("DOMESTIC PARTNER", "Domestic Partner"),
            ("SON", "Son"),
            ("DAUGHTER", "Daughter"),
            ("FATHER", "Father"),
            ("MOTHER", "Mother"), 
            ("FATHER IN LAW", "Father in law"), 
            ("MOTHER IN LAW", "Mother in Law"),
            ("FIANCE", "Fiance"),
            ("FRIEND", "Friend"),
            ("OTHER", "Other"),
        ),
    )

    Driver_Relation = models.CharField(driver_relation_options, max_length=50)

    state_options = (
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DC", "Washington D.C."),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
    )

    Drivers_License_State = models.CharField(state_options, max_length=30)

    Drivers_License_Number = models.CharField(max_length=30)

    drivers_license_options = (
        ("ACTIVE LICENSE", "Active License"),
        ("LEARNERS PERMIT", "Permit License"),
        ("COMMERCIAL LICENSE", "Commerical License"),
        ("FOREIGN LICENSE", "Foreign License"),
        ("INTERNATION LICENSE", "International License"),
        ("SUSPENDED LICENSE", "Suspended License"),
        ("EXPIRED LICENSE", "Expired License"),
        ("NOT LICENSED TO DRIVE", "Not licensed to drive"),
    )
    Drivers_License_Status = models.CharField(drivers_license_options, max_length=50)

    gender_options = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("NONBINARY", "NonBinary"),
        ("NOANSWER", "Prefer Not to Answer"),
    )
    gender = models.CharField(gender_options, max_length=30)

    date_of_issuance = models.DateField()

    job_status_options = (
        ("FULL_TIME_EMPLOYED", "Full Time Employed"),
        ("PART_TIME_EMPLOYED", "Part Time Employed"),
        ("STUDENT", "Student"),
        ("HOMEMAKER", "Homemaker"),
        ("UNEMPLOYED", "Unemployed"),
    )

    job_status = models.CharField(job_status_options, max_length=50)

    education_options = (
        ("LESS THAN HIGHSCHOOL", "Less than highschool"),
        ("HIGHSCHOOL", "Highschool"),
        ("VOCATIONAL", "Vocational"),
        ("ASSOCIATE", "Associate"),
        ("Bachelors", "Bachelors"),
        ("PHD", "Phd"),
        ("DOCTORS", "Doctor"),
        ("LAWYER", "Lawyer"),
    )
    education = models.CharField(education_options, max_length=35)

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
    Vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Drivers = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    Reference_Number = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=7, decimal_places=2)


