from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from Hall_Admin.views import *
from Varsity_Admin.models import *
from Provost.models import *
from Student.models import *
from Staff.models import *
from Hall_Admin.models import *
class HallAdminViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

        # Create a test hall admin associated with the test user
        self.hall_admin = HallAdmin.objects.create(email=self.user.email,username=self.user.username)
        provost=Provost.objects.create(provostId=100,email='provsot@gmail.com',username='provost',password='pass')
        # Create a test hall associated with the test hall admin
        self.hall = Hall.objects.create(hallAdmin=self.hall_admin,provost=provost)

        # Create some test rooms associated with the test hall
        Room.objects.create(hall=self.hall, roomId=101, capacity=10, color='crimson')
        Room.objects.create(hall=self.hall, roomId=201, capacity=10, color='crimson')
        Room.objects.create(hall=self.hall, roomId=301, capacity=10, color='crimson')

        # Create a request object
        self.factory = RequestFactory()

    def test_hall_admin_view(self):
        # Create a GET request
        request = self.factory.get('/hallAdmin')
        request.user = self.user

        # Attach the session to the request (required for authentication)
        request.session = self.client.session

        # Add test data to the session if needed

        # Call the view function
        response = hallAdmin(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Add more assertions if needed to verify the content of the response
