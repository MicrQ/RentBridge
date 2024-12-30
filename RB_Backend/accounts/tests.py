from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountTests(TestCase):
    """ tests for user model """

    @classmethod
    def setUpTestData(cls):
        """ setting up data for testing """
        UserModel = get_user_model()
        cls.user = UserModel.objects.create_user(
            email="test@user.com",
            firstname="test",
            lastname="user",
            password="testpassword"
        )
        cls.superuser = UserModel.objects.create_superuser(
            email="admin@user.com",
            firstname="admin",
            lastname="user",
            password="pass@123"
        )

    def test_customuser_model(self):
        """ test user model """
        self.assertEqual(self.user.email, "test@user.com")
        self.assertEqual(self.user.firstname, "test")
        self.assertEqual(self.user.lastname, "user")
        self.assertFalse(self.user.is_staff, False)

    def test_superuser_creation(self):
        """ test superuser creation """
        self.assertEqual(self.superuser.email, "admin@user.com")
        self.assertEqual(self.superuser.firstname, "admin")
        self.assertEqual(self.superuser.lastname, "user")
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)


class AccountViewsTests(TestCase):
    """ tests for account views """
    def test_user_registration_view(self):
        """ test user registration view """
        response = self.client.post(
            '/api/v1/accounts/register/',
            {
                'email': 'test@user.com',
                'firstname': 'test',
                'lastname': 'user',
                'password': 'testpassword'
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'],
                         'User registered successfully')
        self.assertTrue('token' in response.data)

    def test_user_login_view(self):
        """ test user login view """
        user = AccountTests().superuser
        self.test_user_registration_view()
        response = self.client.post(
            '/api/v1/accounts/login/',
            {
                'email':  'test@user.com',
                'password': 'testpassword'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'],
                         'Logged in successfully')
        self.assertTrue('token' in response.data)

        return response.data['token']
