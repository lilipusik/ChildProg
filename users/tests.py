from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        self.register_path = reverse('users:register')
        self.login_path = reverse('users:login')
        self.data = {
            'first_name': 'Oleg',
            'last_name': 'Ivanov',
            'username': 'Olezha',
            'email': 'oleg@mail.ru',
            'password1': 'OlezhaIvan123987',
            'password2': 'OlezhaIvan123987'
        }

    def test_user_registration_get(self):
        response = self.client.get(self.register_path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_user_registration_post_success(self):
        response = self.client.post(self.register_path, self.data)
        username = self.data['username']
        # self.assertFalse(User.objects.filter(username=username).exists())
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_login_after_registration(self):
        self.client.post(self.register_path, self.data)
        login_data = {
            'username': self.data['username'],
            'password': self.data['password1'],
        }
        response = self.client.post(self.login_path, login_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

