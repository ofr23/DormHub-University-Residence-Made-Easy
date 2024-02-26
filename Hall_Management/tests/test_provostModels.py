from django.db import IntegrityError
from django.test import TestCase
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import * # Update path based on model location


class ProvostModelTests(TestCase):

    def test_create_provost(self):
        """Tests creating a Provost instance with valid data."""
        provost = Provost.objects.create(email="test@example.com")
        self.assertEqual(provost.email, "test@example.com")
        self.assertEqual(provost.username, "None")
        self.assertEqual(provost.password, "None")

    def test_unique_email(self):
        """Tests the uniqueness of the email field."""
        Provost.objects.create(email="unique@example.com")
        with self.assertRaises(IntegrityError):
            Provost.objects.create(email="unique@example.com")

    def test_string_representation(self):
        """Tests the __str__ method for clarity and correctness."""
        provost = Provost.objects.create(email="johndoe@example.com")
        self.assertEqual(str(provost), "johndoe@example.com")

    def test_blank_null_fields(self):
        """Tests that optional fields can be blank or null."""
        provost = Provost.objects.create(email="test@example.com", name="John Doe", username="johndoe")
        self.assertEqual(provost.name, "John Doe")
        self.assertEqual(provost.username, "johndoe")
