from django.db import IntegrityError
from django.test import TestCase
from Hall_Admin.models import *
from Varsity_Admin.models import *
from ..models import *
 # Update path based on model location
import datetime

class StaffModelTests(TestCase):

    def test_create_staff(self):
        """Tests creating a Staff instance with valid data."""
        hallAdmin=HallAdmin.objects.create(
            username='admin',
            adminId=1,
            email='admin@example.com',
            password='password'

        )
        provost=Provost.objects.create(
            provostId=1,
            username='provost',
            email='provost@example.com',
            password='password'
        )
        hall = Hall.objects.create(hallId=1,name="Test Hall",hallAdmin=hallAdmin,provost=provost)  # Create a Hall instance first
        staff = Staff.objects.create(email="test@example.com", name="John Doe", username="johndoe", password="password",hall=hall)
        self.assertEqual(staff.email, "test@example.com")
        self.assertEqual(staff.name, "John Doe")
        self.assertEqual(staff.username, "johndoe")
        self.assertEqual(staff.password, "password")
        self.assertEqual(staff.hall, hall)

    def test_unique_email(self):
        """Tests the uniqueness of the email field."""
        hallAdmin=HallAdmin.objects.create(
            username='admin',
            adminId=1,
            email='admin@example.com',
            password='password'

        )
        provost=Provost.objects.create(
            provostId=1,
            username='provost',
            email='provost@example.com',
            password='password'
        )
        hall = Hall.objects.create(hallId=1,name="Test Hall",hallAdmin=hallAdmin,provost=provost)  # Create a Hall instance first
        staff = Staff.objects.create(email="test@example.com", name="John Doe", username="johndoe", password="password",hall=hall)
        with self.assertRaises(IntegrityError):
            Staff.objects.create(email="test@example.com")

    def test_blank_optional_fields(self):
        """Tests that optional fields can be blank or null."""
        hallAdmin=HallAdmin.objects.create(
            username='admin',
            adminId=1,
            email='admin@example.com',
            password='password'

        )
        provost=Provost.objects.create(
            provostId=1,
            username='provost',
            email='provost@example.com',
            password='password'
        )
        hall = Hall.objects.create(hallId=1,name="Test Hall",hallAdmin=hallAdmin,provost=provost)  # Create a Hall instance first
        staff = Staff.objects.create(email="test@example.com",name='John Doe', username='johndoe' ,hall=hall)
        self.assertEqual(staff.name,'John Doe')
        self.assertEqual(staff.username,'johndoe')

    # Add more test cases for Staff as needed (e.g., validation rules, foreign key constraints)

class VisitorModelTests(TestCase):

    def test_create_visitor(self):
        """Tests creating a Visitor instance with valid data."""
        hallAdmin=HallAdmin.objects.create(
            username='admin',
            adminId=1,
            email='admin@example.com',
            password='password'

        )
        provost=Provost.objects.create(
            provostId=1,
            username='provost',
            email='provost@example.com',
            password='password'
        )
        hall = Hall.objects.create(hallId=1,name="Test Hall",hallAdmin=hallAdmin,provost=provost)
        visitor = Visitor.objects.create(hall=hall, visitorId=123, date=datetime.date.today(), name="John Doe", phone="1234567890")
        self.assertEqual(visitor.hall, hall)
        self.assertEqual(visitor.visitorId, 123)
        self.assertEqual(visitor.date, datetime.date.today())
        self.assertEqual(visitor.name, "John Doe")
        self.assertEqual(visitor.phone, "1234567890")

    def test_foreign_key_constraint(self):
        """Tests that Visitor cannot be created without a ForeignKey to Hall."""
        with self.assertRaises(IntegrityError):
            Visitor.objects.create(visitorId=123, name="John Doe")

    def test_optional_fields(self):
        """Tests that optional fields can be blank or null."""
        hallAdmin=HallAdmin.objects.create(
            username='admin',
            adminId=1,
            email='admin@example.com',
            password='password'

        )
        provost=Provost.objects.create(
            provostId=1,
            username='provost',
            email='provost@example.com',
            password='password'
        )
        hall = Hall.objects.create(hallId=1,name="Test Hall",hallAdmin=hallAdmin,provost=provost)
        visitor = Visitor.objects.create(hall=hall, visitorId=123, date=datetime.date.today())
        self.assertEqual(visitor.name, None)
        self.assertEqual(visitor.phone, None)
        self.assertEqual(visitor.visit, None)
        self.assertEqual(visitor.arrival, None)
        self.assertEqual(visitor.departure, None)
