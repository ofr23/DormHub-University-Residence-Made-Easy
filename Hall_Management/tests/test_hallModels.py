from django.db import IntegrityError
from django.test import TestCase
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *


class VarsityAdminModelTests(TestCase):

    def test_create_varsity_admin(self):
        """Tests creating a VarsityAdmin instance with valid data."""
        admin = VarsityAdmin.objects.create(email="test@example.com")
        self.assertEqual(admin.email, "test@example.com")
        self.assertEqual(admin.username, "NOne")
        self.assertEqual(admin.password, "None")

    def test_blank_optional_fields(self):
        """Tests that optional fields can be blank or null."""
        admin = VarsityAdmin.objects.create(email="valid@example.com", name="John Doe", username="johndoe")
        self.assertEqual(admin.name, "John Doe")
        self.assertEqual(admin.username, "johndoe")

    # Add more test cases for VarsityAdmin as needed (e.g., validation rules)


class HallModelTests(TestCase):

    def setUp(self):
        # Create required objects (provost, hall admin)
        provost = Provost.objects.create(email="provost@example.com")
        hall_admin = HallAdmin.objects.create(email="halladmin@example.com")
        self.provost = provost
        self.hall_admin = hall_admin

    def test_create_hall(self):
        """Tests creating a Hall instance with valid data and relationships."""
        hall = Hall.objects.create(name="Test Hall", hallAdmin=self.hall_admin, provost=self.provost)
        self.assertEqual(hall.name, "Test Hall")
        self.assertEqual(hall.hallAdmin, self.hall_admin)
        self.assertEqual(hall.provost, self.provost)

    def test_string_representation(self):
        """Tests the __str__ method for clarity and correctness."""
        hall = Hall.objects.create(name="Test Hall", hallId=123, hallAdmin=self.hall_admin, provost=self.provost)
        self.assertEqual(str(hall), "Test Hall - 123")

    # Add more test cases for Hall as needed (e.g., unique constraints, field limitations)

class RoomModelTests(TestCase):

    def setUp(self):
        # Create required objects (hall)
        hall = Hall.objects.create(name="Test Hall", hallAdmin=HallAdmin.objects.create(email="halladmin@example.com"),
                                   provost=Provost.objects.create(email="provost@example.com"))
        self.hall = hall

    def test_create_room(self):
        """Tests creating a Room instance with valid data and relationships."""
        room = Room.objects.create(roomId=101, capacity=20, hall=self.hall, color="blue")
        self.assertEqual(room.roomId, 101)
        self.assertEqual(room.capacity, 20)
        self.assertEqual(room.hall, self.hall)

    # def test_foreign_key_constraint(self):
    #     """Tests that Room cannot be created without a ForeignKey to Hall."""
    #     with self.assertRaises(IntegrityError):
    #         Room.objects.create(roomId=102, capacity=30)  # Missing hall

    def test_string_representation(self):
        """Tests the __str__ method for clarity and correctness."""
        room = Room.objects.create(roomId=102, capacity=30, hall=self.hall, color="green")
        self.assertEqual(str(room), "102 - 0")
