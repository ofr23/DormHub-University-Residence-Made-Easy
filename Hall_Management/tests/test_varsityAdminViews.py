from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
from Varsity_Admin.views import *
class VarsityAdminViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.provost = Provost.objects.create(email='provost@example.com')  # Create a sample Provost
        self.admin = HallAdmin.objects.create(email='admin@example.com')    # Create a sample Hall Admin
        self.staff = Staff.objects.create(email='staff@example.com')        # Create a sample Staff member

    def test_add_session(self):
        request = self.factory.post('/varsityAdmin', {'session': '', 'sess': '2023', 'csv': 'sample.csv'})
        response = varsityAdmin(request)
        self.assertEqual(response.status_code, 302)  # Ensure redirection after adding a session
        # self.assertTrue(Session.objects.filter(session='2023', csvFile='sample.csv').exists())  # Check if session is added

    def test_add_hall(self):
        request = self.factory.post('/varsityAdmin', {'hall': '', 'id': '1', 'name': 'Sample Hall', 'provost': self.provost.email, 'admin': self.admin.email})
        response = varsityAdmin(request)
        self.assertEqual(response.status_code, 302)  # Ensure redirection after adding a hall
        self.assertTrue(Hall.objects.filter(hallId=1, name='Sample Hall', provost=self.provost, hallAdmin=self.admin).exists())  # Check if hall is added

    def test_render_template(self):
        request = self.factory.get('/varsityAdmin')
        response = varsityAdmin(request)
        self.assertEqual(response.status_code, 200)  # Ensure template is rendered successfully

    # Add more test methods to cover edge cases, validation, and error handling
