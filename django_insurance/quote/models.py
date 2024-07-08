from django.db import models

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
    Usage_Type = models.CharField(choices=Usage_Type_Options, max_length=11, blank=True)
    Annual_Mileage = models.IntegerField()
    Year = models.IntegerField(max_length=4)
    Make = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)


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
