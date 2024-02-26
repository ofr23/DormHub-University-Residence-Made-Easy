from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
from Student.views import *
from django.urls import reverse

class StudentViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='teststudent', email='student@example.com', password='password')
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        provost = Provost.objects.create(email=self.user.email)
        # Create a test hall
        self.hall = Hall.objects.create(hallId=1,hallAdmin=hallAdmin,provost=provost)
        room=Room.objects.create(hall=self.hall)
        # Create a test student associated with the test user
        self.student = Student.objects.create(email=self.user.email,hall=self.hall,room=room)

        # Create a request factory
        self.factory = RequestFactory()

    def test_student_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('student'))
        request.user = self.user

        # Call the view function
        response = student(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'student.html')

    def test_student_view_post_swap_request(self):
        # Create a POST request with 'change' parameter
        request = self.factory.post(reverse('student'), {'change': True, 'reason': 'Reason for swap request'})
        request.user = self.user

        # Call the view function
        response = student(request)

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect goes to the expected URL
        self.assertEqual(response.url, '/student')

        # Check that a swap request is created
        self.assertEqual(SwapRequest.objects.filter(student=self.student, hall=self.hall).count(), 1)

    def test_student_view_post_repair_request(self):
        # Create a POST request with 'repair' parameter
        request = self.factory.post(reverse('student'), {'repair': True, 'reason': 'Reason for repair request', 'type': 1})
        request.user = self.user

        # Call the view function
        response = student(request)

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect goes to the expected URL
        self.assertEqual(response.url, '/student')

        # Check that a repair request is created
        self.assertEqual(RepairRequest.objects.filter(student=self.student, hall=self.hall).count(), 1)

    # Add more tests for student view as needed
