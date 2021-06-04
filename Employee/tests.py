from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersTests(TestCase):
    """
    Test Case to check for the users created
    """
    def test_create_user(self):
        employee = get_user_model()
        user = employee.objects.create_user(emp_id=10001, password='foo')
        self.assertEqual(user.emp_id, 10001)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            employee.objects.create_user()
        with self.assertRaises(TypeError):
            employee.objects.create_user(emp_id=None)
        with self.assertRaises(ValueError):
            employee.objects.create_user(emp_id=None, password="foo")

    def test_create_superuser(self):
        employee = get_user_model()
        admin_user = employee.objects.create_superuser(10000, 'foo')
        self.assertEqual(admin_user.emp_id, 10000)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.role, 0)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            employee.objects.create_superuser(emp_id=10000, password='foo', is_superuser=False)

