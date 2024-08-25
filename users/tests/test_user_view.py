from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User

class TestUserView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'jdoe@j.com',
            'password': 'password',
            'user_type': 'admin'
        }

    def test_register_user(self):
        # Use the client to send a POST request to the register endpoint
        response = self.client.post(reverse('register_user'), self.user_data, format='json')

        # Assert that the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that a user was created in the database
        self.assertEqual(User.objects.count(), 1)

        # Retrieve the created user and assert the data
        user = User.objects.get()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'jdoe@j.com')

    def destroy_user(self):
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
