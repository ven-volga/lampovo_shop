from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationTest(TestCase):
    def test_user_registration_creates_inactive_user(self):
        response = self.client.post(reverse('register'), {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(email='test@example.com')
        self.assertFalse(user.is_active)




