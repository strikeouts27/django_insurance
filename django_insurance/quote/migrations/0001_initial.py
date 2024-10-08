# Generated by Django 5.0.7 on 2024-08-26 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('zip_code', models.CharField(default=0, max_length=10)),
                ('email_address', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('home_ownership', models.CharField(choices=[('OWN', 'Owns_Property'), ('RENT', 'Rents_Property')], max_length=50)),
                ('suffix', models.CharField(blank=True, max_length=10)),
                ('apt_number', models.CharField(blank=True, max_length=10)),
                ('quote_id', models.CharField(blank=True, max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_first_name', models.CharField(max_length=50, null=True)),
                ('driver_last_name', models.CharField(max_length=50, null=True)),
                ('driver_relation', models.CharField(choices=[('SELF', 'Self'), ('GRANDFATHER', 'Grandfather'), ('GRANDMOTHER', 'Grandmother'), ('SPOUSE', 'Spouse'), ('DOMESTIC PARTNER', 'Domestic Partner'), ('SON', 'Son'), ('DAUGHTER', 'Daughter'), ('FATHER', 'Father'), ('MOTHER', 'Mother'), ('FATHER IN LAW', 'Father in law'), ('MOTHER IN LAW', 'Mother in Law'), ('FIANCE', 'Fiance'), ('FRIEND', 'Friend'), ('OTHER', 'Other')], default='SELF', max_length=16, null=True)),
                ('quote_id', models.CharField(blank=True, max_length=11)),
                ('drivers_license_state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'Washington D.C.'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=30, null=True)),
                ('drivers_license_number', models.CharField(max_length=30, null=True)),
                ('drivers_license_status', models.CharField(choices=[('ACTIVE LICENSE', 'Active License'), ('LEARNERS PERMIT', 'Permit License'), ('COMMERCIAL LICENSE', 'Commerical License'), ('FOREIGN LICENSE', 'Foreign License'), ('INTERNATION LICENSE', 'International License'), ('SUSPENDED LICENSE', 'Suspended License'), ('EXPIRED LICENSE', 'Expired License'), ('NOT LICENSED TO DRIVE', 'Not licensed to drive')], max_length=50, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NONBINARY', 'NonBinary'), ('NOANSWER', 'Prefer Not to Answer')], max_length=30)),
                ('date_of_issuance', models.DateField()),
                ('job_status', models.CharField(choices=[('FULL_TIME_EMPLOYED', 'Full Time Employed'), ('PART_TIME_EMPLOYED', 'Part Time Employed'), ('STUDENT', 'Student'), ('HOMEMAKER', 'Homemaker'), ('UNEMPLOYED', 'Unemployed')], max_length=50)),
                ('education', models.CharField(choices=[('LESS THAN HIGHSCHOOL', 'Less than highschool'), ('HIGHSCHOOL', 'Highschool'), ('VOCATIONAL', 'Vocational'), ('ASSOCIATE', 'Associate'), ('Bachelors', 'Bachelors'), ('PHD', 'Phd'), ('DOCTORS', 'Doctor'), ('LAWYER', 'Lawyer')], max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Identification_Number', models.CharField(max_length=30)),
                ('Used_For_Ride_Sharing', models.CharField(blank=True, max_length=10)),
                ('Usage_Type', models.CharField(blank=True, choices=[('PLEASURE', 'Pleasure Vehicle'), ('WORK', 'Work/School'), ('BUSINESS', 'Business'), ('COMMERCIAL', 'Commercial')], max_length=11)),
                ('Annual_Mileage', models.CharField(choices=[('0 - 3,999', '0 - 3,999'), ('4,000 - 5,999', '4,000 - 5,999'), ('6,000 - 7,999', '6,000 - 7,999'), ('8,000 - 9,999', '8,000 - 9,999'), ('10,000 - 11,999', '10,000 - 11,999'), ('12,000 - 13,999', '12,000 - 13,999'), ('14,000 - 15,999', '14,000 - 15,999'), ('16,000 - 17,999', '16,000 - 17,999'), ('18,000 - 19,999', '18,000 - 19,999'), ('20,000 OR MORE', '20,000 or more')], max_length=15)),
                ('Year', models.IntegerField()),
                ('Make', models.CharField(max_length=30)),
                ('quote_id', models.CharField(blank=True, max_length=11)),
                ('Model', models.CharField(max_length=30)),
                ('Vehicle_Ownership', models.CharField(choices=[('FINANCE', 'Finance'), ('OWN', 'Own'), ('LEASE', 'Lease')], max_length=11)),
                ('Vehicle_Ownership_Timeframe', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reference_Number', models.CharField(max_length=30)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.customer')),
                ('Driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.driver')),
                ('Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.vehicle')),
            ],
        ),
    ]
