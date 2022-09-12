from django.test import TestCase
from django.db.utils import IntegrityError

from users.models import User

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.user_data = {
            "username": "victoria",
            "password": "1234",
            "first_name": "Victoria",
            "last_name": "Viana",
            "email": "victoria@email.com"
        }

        cls.user = User.objects.create(**cls.user_data)

    def test_unique_constraints_in_username_and_email_fields(self):
        print("test_unique_constraints_in_username_and_email_fields")

        with self.assertRaises(IntegrityError):
            user_example = {
                "username": "victoria",
                "password": "1234",
                "first_name": "Victoria",
                "last_name": "Viana",
                "email": "victoria@email.com"
            }

            User.objects.create_user(**user_example)

    def test_equality_of_some_user_fields(self):
        print("test_equality_of_some_user_fields")

        self.assertEqual(self.user.username, self.user_data["username"])
        self.assertEqual(self.user.email, self.user_data["email"])
        self.assertEqual(self.user.first_name, self.user_data["first_name"])
        self.assertEqual(self.user.last_name, self.user_data["last_name"])