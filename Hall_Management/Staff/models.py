"""
Django Models Documentation

This module defines models representing staff members and visitors.
"""

from django.db import models
from Varsity_Admin.models import Hall  # Import the Hall model
import datetime


class Staff(models.Model):
    """
    Model representing staff members.

    Attributes:
        name (CharField): The name of the staff member.
        email (EmailField): The email address of the staff member (unique).
        username (CharField): The username of the staff member.
        password (CharField): The password of the staff member.
        hall (ForeignKey): The hall associated with the staff member.
    """

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE,null=True)

    def __str__(self):
        """
        String representation of the Staff object.

        Returns:
            str: The email address of the staff member.
        """
        return str(self.email)


class Visitor(models.Model):
    """
    Model representing visitors.

    Attributes:
        hall (ForeignKey): The hall associated with the visitor.
        visitorId (IntegerField): The ID of the visitor.
        date (DateField): The date of the visit.
        name (CharField): The name of the visitor.
        phone (CharField): The phone number of the visitor.
        visit (CharField): The purpose of the visit.
        arrival (TimeField): The arrival time of the visitor.
        departure (TimeField): The departure time of the visitor.
    """

    hall = models.ForeignKey(Hall, on_delete=models.CASCADE,null=True)
    visitorId = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.datetime.now().date())
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    visit = models.CharField(max_length=100, null=True, blank=True)
    arrival = models.TimeField(null=True, blank=True)
    departure = models.TimeField(null=True, blank=True)

    def __str__(self):
        """
        String representation of the Visitor object.

        Returns:
            str: A string containing the date and visitor ID.
        """
        return str(self.date) + " - " + str(self.visitorId)
