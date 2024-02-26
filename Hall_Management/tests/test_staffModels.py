"""
Django Model Tests Documentation

This module contains tests for the Staff and Visitor models. These tests ensure the integrity and functionality
of the models under various scenarios.
"""

import datetime

from Hall_Admin.models import HallAdmin
from Varsity_Admin.models import *
from django.db import IntegrityError
from django.test import TestCase
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
  # Update path based on model location


class StaffModelTests(TestCase):
    """
    Tests for the Staff model.
    """

    def test_create_staff(self):
        """
        Test creating a Staff instance with valid data.

        This test verifies that a Staff instance can be created with valid data,
        including the necessary related instances such as Hall, HallAdmin, and Provost.
        """
        # Create necessary related instances
        hall_admin = HallAdmin.objects.create(username='admin', adminId=1, email='admin@example.com',
                                              password='password')
        provost = Provost.objects.create(provostId=1, username='provost', email='provost@example.com',
                                         password='password')
        hall = Hall.objects.create(hallId=1, name="Test Hall", hallAdmin=hall_admin, provost=provost)

        # Create Staff instance
        staff = Staff.objects.create(email="test@example.com", name="John Doe", username="johndoe", password="password",
                                     hall=hall)

        # Assert expected values
        self.assertEqual(staff.email, "test@example.com")
        self.assertEqual(staff.name, "John Doe")
        self.assertEqual(staff.username, "johndoe")
        self.assertEqual(staff.password, "password")
        self.assertEqual(staff.hall, hall)

    def test_unique_email(self):
        """
        Test the uniqueness of the email field.

        This test ensures that the email field in the Staff model is unique.
        """
        # Create necessary related instances
        hall_admin = HallAdmin.objects.create(username='admin', adminId=1, email='admin@example.com',
                                              password='password')
        provost = Provost.objects.create(provostId=1, username='provost', email='provost@example.com',
                                         password='password')
        hall = Hall.objects.create(hallId=1, name="Test Hall", hallAdmin=hall_admin, provost=provost)

        # Create Staff instance with existing email
        Staff.objects.create(email="test@example.com", name="John Doe", username="johndoe", password="password",
                             hall=hall)

        # Attempt to create another Staff instance with the same email (should raise IntegrityError)
        with self.assertRaises(IntegrityError):
            Staff.objects.create(email="test@example.com")

    # def test_blank_optional_fields(self):
    #     """
    #     Test that optional fields can be blank or null.

    #     This test verifies that optional fields in the Staff model, such as 'name' and 'username',
    #     can be left blank or set to None.
    #     """
    #     # Create necessary related instances
    #     hall_admin = HallAdmin.objects.create(username='admin', adminId=1, email='admin@example.com',
    #                                           password='password')
    #     provost = Provost.objects.create(provostId=1, username='provost', email='provost@example.com',
    #                                      password='password')
    #     hall = Hall.objects.create(hallId=1, name="Test Hall", hallAdmin=hall_admin, provost=provost)

    #     # Create Staff instance with blank optional fields
    #     staff = Staff.objects.create(email="test@example.com", name=None, username=None, hall=hall)

    #     # Assert expected values
    #     self.assertIsNone(staff.name)
    #     self.assertIsNone(staff.username)


class VisitorModelTests(TestCase):
    """
    Tests for the Visitor model.
    """

    def test_create_visitor(self):
        """
        Test creating a Visitor instance with valid data.

        This test verifies that a Visitor instance can be created with valid data,
        including the necessary related instances such as Hall.
        """
        # Create necessary related instances
        hall_admin = HallAdmin.objects.create(username='admin', adminId=1, email='admin@example.com',
                                              password='password')
        provost = Provost.objects.create(provostId=1, username='provost', email='provost@example.com',
                                         password='password')
        hall = Hall.objects.create(hallId=1, name="Test Hall", hallAdmin=hall_admin, provost=provost)

        # Create Visitor instance
        visitor = Visitor.objects.create(hall=hall, visitorId=123, date=datetime.date.today(), name="John Doe",
                                         phone="1234567890")

        # Assert expected values
        self.assertEqual(visitor.hall, hall)
        self.assertEqual(visitor.visitorId, 123)
        self.assertEqual(visitor.date, datetime.date.today())
        self.assertEqual(visitor.name, "John Doe")
        self.assertEqual(visitor.phone, "1234567890")

    # def test_foreign_key_constraint(self):
    #     """
    #     Test that Visitor cannot be created without a ForeignKey to Hall.

    #     This test ensures that a Visitor instance cannot be created without
    #     a ForeignKey reference to a Hall instance.
    #     """
    #     # Attempt to create Visitor without a Hall ForeignKey (should raise IntegrityError)
    #     with self.assertRaises(IntegrityError):
    #         Visitor.objects.create(visitorId=123, name="John Doe")

    def test_optional_fields(self):
        """
        Test that optional fields can be blank or null.

        This test verifies that optional fields in the Visitor model, such as 'name' and 'phone',
        can be left blank or set to None.
        """
        # Create necessary related instances
        hall_admin = HallAdmin.objects.create(username='admin', adminId=1, email='admin@example.com',
                                              password='password')
        provost = Provost.objects.create(provostId=1, username='provost', email='provost@example.com',
                                         password='password')
        hall = Hall.objects.create(hallId=1, name="Test Hall", hallAdmin=hall_admin, provost=provost)

        # Create Visitor instance with blank optional fields
        visitor = Visitor.objects.create(hall=hall, visitorId=123, date=datetime.date.today())

        # Assert expected values
        self.assertIsNone(visitor.name)
        self.assertIsNone(visitor.phone)
        self.assertIsNone(visitor.visit)
        self.assertIsNone(visitor.arrival)
        self.assertIsNone(visitor.departure)
