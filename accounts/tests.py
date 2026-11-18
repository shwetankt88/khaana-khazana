from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class RegisterViewTest(TestCase):
    def test_register_page_loads(self):
        resp = self.client.get(reverse('accounts:register'))
        self.assertEqual(resp.status_code, 200)

    def test_register_creates_user(self):
        resp = self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'email': 'new@test.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'pass1234')

    def test_login_page_loads(self):
        resp = self.client.get(reverse('accounts:login'))
        self.assertEqual(resp.status_code, 200)

    def test_login_valid(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'testuser', 'password': 'pass1234'
        })
        self.assertIn(resp.status_code, [200, 302])


class ProfileViewTest(TestCase):
    def test_profile_requires_login(self):
        resp = self.client.get(reverse('accounts:profile'))
        self.assertEqual(resp.status_code, 302)

    def test_profile_logged_in(self):
        User.objects.create_user('chef', 'c@t.com', 'pass1234')
        self.client.login(username='chef', password='pass1234')
        resp = self.client.get(reverse('accounts:profile'))
        self.assertEqual(resp.status_code, 200)
