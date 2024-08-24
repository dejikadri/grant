from django.test import TestCase
from users.user_service import check_user_login
from users.models import User



class TestUserService(TestCase):
    def setUp(self):
       self.user = User.objects.create_user(
            first_name='John',
            last_name='Doe',
            email='jdoe@xyz.com',
            password='pass123',
            user_type='applicant'
        )
       self.test_email = 'jdoe@xyz.com'
       self.test_password = 'pass123'
    
       
    def tearDown(self):
        self.user.delete()
              


    def test_user_exists(self):
        from users.user_service import check_user_exists
        from users.models import User

        self.assertTrue(check_user_exists(self.user.email))
    
    def test_user_login(self):
        self.assertEqual(check_user_login(self.test_email, self.test_password), self.user)
        self.assertIsNone(check_user_login(self.user.email, 'wrong_password'))
        self.assertIsNone(check_user_login('wrong_email', self.user.password))
        self.assertIsNone(check_user_login('wrong_email', 'wrong_password'))

