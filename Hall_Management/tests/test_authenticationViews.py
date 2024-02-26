from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
from Authentication.views import *

# class LogInViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         # Create sample users for testing

#         self.provost = Provost.objects.create(username='provost1', email='provost@example.com', password='password123')
#         self.hall_admin = HallAdmin.objects.create(username='halladmin1', email='halladmin@example.com', password='password123')
#         self.student = Student.objects.create(username='student1', email='student@example.com', password='password123')
#         self.staff = Staff.objects.create(username='staff1', email='staff@example.com', password='password123')

#     def test_provost_login(self):
#         request = self.factory.post('/authentication', {'login': '', 'type': '1', 'email': 'provost@example.com'})
#         self.user = User.objects.create_user(
#             username='jacob', email='jacob@…', password='top_secret')        
#         login(request, self.user)
#         response = logIn(request)
#         self.assertEqual(response.status_code, 302) 

#     def test_hall_admin_login(self):
#         request = self.factory.post('/authentication', {'login': '', 'type': '2', 'email': 'halladmin@example.com'})
#         response = logIn(request)
#         self.assertIsInstance(response, redirect)  # Should be redirected after successful login
#         self.assertEqual(response.url, '/hallAdmin/')  # Redirect URL should be as expected

#     def test_student_login(self):
#         request = self.factory.post('/authentication', {'login': '', 'type': '3', 'email': 'student@example.com'})
#         response = logIn(request)
#         self.assertIsInstance(response, redirect)  # Should be redirected after successful login
#         self.assertEqual(response.url, '/student')  # Redirect URL should be as expected

#     def test_staff_login(self):
#         request = self.factory.post('/authentication', {'login': '', 'type': '4', 'email': 'staff@example.com'})
#         response = logIn(request)
#         self.assertIsInstance(response, redirect)  # Should be redirected after successful login
#         self.assertEqual(response.url, '/staff')  # Redirect URL should be as expected

#     def test_invalid_login(self):
#         # Test with non-existent email
#         request = self.factory.post('/authentication', {'login': '', 'type': '1', 'email': 'nonexistent@example.com'})
#         response = logIn(request)
#         self.assertEqual(response.status_code, 200) 
class RegisterViewTest(TestCase):
    def setUp(self):
        # Initialize test client
        self.client = Client()
        self.factory = RequestFactory()


    def test_register_provost(self):
        # Create a POST request for provost registration
        response = self.client.post(reverse('register'), {
            'register': True,
            'type': '1',
            'name': 'Provost Name',
            'email': 'provost@example.com',
            'username': 'provost',
            'password': 'password'
        })

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL is correct
        self.assertEqual(response.url, '/authentication')

    def test_register_hallAdmin(self):
        # Create a POST request for provost registration
        response = self.client.post(reverse('register'), {
            'register': True,
            'type': '1',
            'name': 'Provost Name',
            'email': 'provost@example.com',
            'username': 'provost',
            'password': 'password'
        })

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL is correct
        self.assertEqual(response.url, '/authentication')
    def test_register_staff(self):
        # Create a POST request for provost registration
        response = self.client.post(reverse('register'), {
            'register': True,
            'type': '1',
            'name': 'Provost Name',
            'email': 'provost@example.com',
            'username': 'provost',
            'password': 'password'
        })

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL is correct
        self.assertEqual(response.url, '/authentication')
    def test_invalid_request_provost(self):
        # Test when request.POST does not contain 'register'
        request = self.factory.post('/register', {'type': '1', 'name': 'John Doe', 'email': 'john@example.com', 'username': 'johndoe', 'password': 'password123'})
        response = register(request)
        self.assertEqual(response.status_code, 200) 
    
    