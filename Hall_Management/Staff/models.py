from django.db import models
from Varsity_Admin.models import * # Import the Hall model
import datetime


class Staff(models.Model):
    """
    Model representing staff members.
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Staff object (email).
        """
        return str(self.email)


class Visitor(models.Model):
    """
    Model representing visitors.
    """
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    visitorId = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.datetime.now().date())
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    visit = models.CharField(max_length=100, null=True, blank=True)
    arrival = models.TimeField(null=True, blank=True)
    departure = models.TimeField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Visitor object (date and visitorId).
        """
        return str(self.date) + " - " + str(self.visitorId)
