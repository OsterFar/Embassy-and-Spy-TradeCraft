from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class User(models.Model):
    genders = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Others', 'others'),
    )

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=genders, default='Others')
    address = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15, validators=[RegexValidator(r'^\d\d\d\d\d-\d\d\d\d\d\d\d-\d$')])
    country = CountryField(blank_label='Select Country')

    def __str__(self):
        return self.fname


class Employee(models.Model):
    emp_id = models.PositiveIntegerField(primary_key=True)
    country_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.emp_id)


class Spy(models.Model):
    spy_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code_name = models.CharField(unique=True, max_length=30)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_name


class Diplomat(models.Model):
    ranks = (
        ('Ambassador', 'ambassador'),
        ('Minister', 'minister'),
        ("Chargé d'affaires", "Chargé d'affaires"),
    )
    dip_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50, choices=ranks, default="Chargé d'affaires")
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.dip_id


class Agent(models.Model):
    agent_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code_name = models.CharField(unique=True, max_length=30)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_name


class Asset(models.Model):
    asset_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code_name = models.CharField(max_length=30)
    spy_id = models.ForeignKey(Spy, on_delete=models.CASCADE)

    def __str__(self):
        return self.code_name


class Cntry(models.Model):
    country_name = CountryField(primary_key=True)

    def __str__(self):
        return str(self.country_name)
