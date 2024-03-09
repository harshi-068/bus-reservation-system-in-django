# Create your models here.
from django.db import models
from .models import *


# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=10)
    rem = models.DecimalField(decimal_places=0, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email





class Register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "Register"


class Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'

    TICKET_STATUSES = (
        (BOOKED, 'Booked'),
        (CANCELLED, 'Cancelled'),
    )

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid = models.DecimalField(decimal_places=0, max_digits=10)
    busid = models.DecimalField(decimal_places=0, max_digits=10)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=10)

    def __str__(self):
        return self.email
