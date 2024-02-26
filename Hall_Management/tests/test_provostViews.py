from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
from django.urls import reverse
from Provost.views import *

class ProvostViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testprovost', email='provost@example.com', password='password')
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        self.provost = Provost.objects.create(email=self.user.email)

        # Create a test hall associated with the test provost
        self.hall = Hall.objects.create(provost=self.provost, hallId=1,hallAdmin=hallAdmin)

        # Create some test rooms associated with the test hall
        Room.objects.create(hall=self.hall, roomId=101, capacity=10)
        Room.objects.create(hall=self.hall, roomId=102, capacity=10)
        Room.objects.create(hall=self.hall, roomId=103, capacity=10)

        # Create some test students associated with the test hall
        Student.objects.create(studentId=1, hall=self.hall, name='Student 1', email='student1@example.com')
        Student.objects.create(studentId=2, hall=self.hall, name='Student 2', email='student2@example.com')
        Student.objects.create(studentId=3, hall=self.hall, name='Student 3', email='student3@example.com')

        # Create a request factory
        self.factory = RequestFactory()

    def test_provost_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('provost'))
        request.user = self.user

        # Call the view function
        response = provost(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # res = self.client.get('/provost')
        # self.assertTemplateUsed(res, 'provost.html')
        

class AddStudentViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testprovost', email='provost@example.com', password='password')
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')

        # Create a test provost associated with the test user
        self.provost = Provost.objects.create(email=self.user.email)

        # Create a test hall associated with the test provost
        self.hall = Hall.objects.create(provost=self.provost, hallId=1,hallAdmin=hallAdmin)

        # Create some test sessions
        Session.objects.create(session=2023)
        Session.objects.create(session=2024)

        # Create a request factory
        self.factory = RequestFactory()

    def test_add_student_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('addStudent'))
        request.user = self.user

        # Call the view function
        response = addStudent(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'allStudent.html')

        # Add more assertions if needed

    # Add more tests for add student view as needed

class SwapRequestsViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testprovost', email='provost@example.com', password='password')
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        self.provost = Provost.objects.create(email=self.user.email)

        # Create a test hall associated with the test provost
        self.hall = Hall.objects.create(provost=self.provost, hallId=1,hallAdmin=hallAdmin)

        # Create some test students associated with the test hall
        student1 = Student.objects.create(studentId=1, hall=self.hall, name='Student 1', email='student1@example.com')
        student2 = Student.objects.create(studentId=2, hall=self.hall, name='Student 2', email='student2@example.com')

        # Create some test swap requests
        SwapRequest.objects.create(hall=self.hall, student=student1, status=0)
        SwapRequest.objects.create(hall=self.hall, student=student2, status=0)

        # Create a request factory
        self.factory = RequestFactory()

    def test_swap_requests_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('swapRequests'))
        request.user = self.user

        # Call the view function
        response = swapRequests(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'swapRequests.html')

        # Add more assertions if needed

    # Add more tests for swap requests view as needed
