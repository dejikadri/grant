# write the necessary test cases  view in users/views.py.
# The test case should test the following:

# The view should be able to register a user
# The view should be able to login a user
# The view should be able to logout a user



from django.test import TestCase
from users.models import User




class TestUserView(TestCase):
    def setUp(self):
        user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'jdoe@j.com',
            'password': 'password',
            'user_type': 'admin'
        }


    def test_register_user(self):
        from users.views import RegisterUser
        from users.models import User
        from users.serializer import UserSerializer
        from rest_framework.request import Request
        from rest_framework.response import Response
        from rest_framework import status

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'jdoe@j.com',
            'password': 'password',
            'user_type': 'admin'
        }
        serialized_data = UserSerializer(data=data)
        request = Request(serialized_data)
        response = RegisterUser().post(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def destroy_user(self):
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)