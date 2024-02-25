from django.db import IntegrityError
from django.test import TestCase
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *

class HallAdminModelTests(TestCase):

    def test_create_hall_admin(self):
        """
        Tests basic creation of a HallAdmin instance with required fields.
        """
        admin = HallAdmin.objects.create(email="test@example.com")
        self.assertEqual(admin.email, "test@example.com")
        self.assertEqual(admin.username, "")  # Assert default value
        self.assertEqual(admin.password, "")  # Assert default value

    def test_null_or_blank_fields(self):
        """
        Tests if optional fields can be null or blank.
        """
        admin = HallAdmin.objects.create(name="John Doe", email="")
        self.assertEqual(admin.name, "John Doe")
        self.assertEqual(admin.email, "")

    def test_unique_email(self):
        """
        Tests that the email field is unique.
        """
        HallAdmin.objects.create(email="unique@example.com")
        with self.assertRaises(IntegrityError):
            HallAdmin.objects.create(email="unique@example.com")

    def test_str_representation(self):
        """
        Tests the __str__ method for clarity and correctness.
        """
        admin = HallAdmin.objects.create(email="johndoe@example.com")
        self.assertEqual(str(admin), "johndoe@example.com")
