from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

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


class EmailConfirmationTest(TestCase):
    def test_email_confirmation_sets_flags_and_logs_in(self):
        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='StrongPass123!',
            is_active=False,
            email_verify=False
        )

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        response = self.client.get(reverse('verify_email', args=[uid, token]))

        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertTrue(user.email_verify)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)







