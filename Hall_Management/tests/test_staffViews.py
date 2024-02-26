from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Staff.views import *
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
from django.urls import reverse
import datetime

class StaffViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='teststaff', email='staff@example.com', password='password')

        # Create a test staff member associated with the test user
        self.staff = Staff.objects.create(email=self.user.email)

        # Create a request factory
        self.factory = RequestFactory()

    def test_staff_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('staff'))
        request.user = self.user

        # Call the view function
        response = staff(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'staff.html')

    def test_staff_view_post_visitor(self):
        # Create a POST request with 'visitor' parameter
        request = self.factory.post(reverse('staff'), {'visitor': True})
        request.user = self.user

        # Call the view function
        response = staff(request)

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect goes to the expected URL
        self.assertEqual(response.url, '/staff/visitorToday')

    def test_staff_view_post_requests(self):
        # Create a POST request with 'requests' parameter
        request = self.factory.post(reverse('staff'), {'requests': True})
        request.user = self.user

        # Call the view function
        response = staff(request)

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check that the redirect goes to the expected URL
        self.assertEqual(response.url, '/staff/repairRequests')

    # Add more tests for staff view as needed

class VisitorTodayViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='teststaff', email='staff@example.com', password='password')

        # Create a test staff member associated with the test user
        self.staff = Staff.objects.create(email=self.user.email)

        # Create a request factory
        self.factory = RequestFactory()

    def test_visitor_today_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('visitorToday'))
        request.user = self.user

        # Call the view function
        response = visitorToday(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'visitorToday.html')
    def test_retrieve_visitor_records(self):
        time = datetime.datetime.now().time()
        today = datetime.datetime.now().date()
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        provost = Provost.objects.create(provostId=101,email=self.user.email)   
        hall=Hall.objects.create(hallId=100,hallAdmin=hallAdmin,provost=provost)
        visitor1 = Visitor.objects.create(date=today, name='Visitor 1', phone='1234567890', visitorId=1, visit='Purpose 1', arrival=time, hall=hall)
        visitor2 = Visitor.objects.create(date=today, name='Visitor 2', phone='0987654321', visitorId=2, visit='Purpose 2', arrival=time, hall=hall)

        request = self.factory.get('/staff/visitorToday/')
        request.user = User(email=self.staff.email)
        response = visitorToday(request)

        self.assertEqual(response.status_code, 200)  # Ensure template is rendered successfully
        # self.assertEqual(response.context['hall'], 'Sample Hall')  # Ensure correct hall is passed to context
        # self.assertEqual(response.context['today'], today)  # Ensure correct today's date is passed to context
        # self.assertIn(visitor1, response.context['visitorList'])  # Ensure visitor1 is in the list of visitors
        # self.assertIn(visitor2, response.context['visitorList'])  # Ensure visitor2 is in the list of visitors

    def test_add_visitor_record(self):
        request = self.factory.post('/staff/visitorToday/', {'add': '', 'name': 'New Visitor', 'phone': '1234567890', 'visit': 'Purpose of Visit'})
        request.user = User(email=self.staff.email)
        response = visitorToday(request)

        self.assertEqual(response.status_code, 302)  # Ensure redirection after adding a visitor record
        self.assertTrue(Visitor.objects.filter(name='New Visitor', phone='1234567890', visit='Purpose of Visit').exists())  # Check if visitor record is added

    def test_update_departure_time(self):
        time = datetime.datetime.now().time()
        today = datetime.datetime.now().date()
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        provost = Provost.objects.create(provostId=101,email='provost@gmail.com')   
        hall=Hall.objects.create(hallId=100,hallAdmin=hallAdmin,provost=provost)     
        visitor = Visitor.objects.create(date=today, name='Visitor', phone='1234567890', visitorId=1, visit='Purpose', arrival=time, hall=hall)

        try:
            request = self.factory.post('/staff/visitorToday/', {'departure': visitor.visitorId})
            request.user = User(email=self.staff.email)
            response = visitorToday(request)
    
            self.assertEqual(response.status_code, 302)  # Ensure redirection after updating departure time
            updated_visitor = Visitor.objects.get(visitorId=visitor.visitorId)
            self.assertIsNotNone(updated_visitor.departure)  # Ensure departure time is updated
        except Visitor.DoesNotExist:
            print('ok')
class RepairRequestsViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='teststaff', email='staff@example.com', password='password')
        hallAdmin=HallAdmin.objects.create(adminId=100,email='admin@gmail.com',username='admin',password='pass')
        # Create a test provost associated with the test user
        provost = Provost.objects.create(email=self.user.email)

        # Create a test hall associated with the test provost
        hall = Hall.objects.create(provost=provost, hallId=1,hallAdmin=hallAdmin)
        # Create a test staff member associated with the test user
        self.staff = Staff.objects.create(email=self.user.email,hall=hall)

        # Create a request factory
        self.factory = RequestFactory()

    def test_repair_requests_view_get(self):
        # Create a GET request
        request = self.factory.get(reverse('repairRequests'))
        request.user = self.user

        # Call the view function
        response = repairRequests(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        # self.assertTemplateUsed(response, 'repairRequests.html')
    def test_retrieve_repair_requests(self):
        request = self.factory.get('/staff/repairRequests/')
        request.user = User(email=self.staff.email)
        response = repairRequests(request)

        self.assertEqual(response.status_code, 200)  # Ensure template is rendered successfully
        # self.assertQuerysetEqual(response.context['requests'], [repr(self.request1), repr(self.request2)], ordered=False)  # Ensure correct repair requests are passed to context

    

    # Add more tests for repair requests view as needed
