from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status, Response

from model_bakery import baker

from users.models import User

class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = "/api/users/"

        [baker.make("users.User") for _ in range(10)]

    def test_can_retrieve_all_users(self):
        print("test_can_retrieve_all_users")

        response: Response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
    
class UserDetailView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        user_data = {
            "username": "victoria",
            "password": "1234",
            "first_name": "Victoria",
            "last_name": "Viana",
            "email": "victoria@email.com"
        }

        admin_data = {
            "username": "admin",
            "password": "supersegura",
            "first_name": "Admin",
            "last_name": "Istradorx",
            "email": "admin@email.com"
        }

        another_user_data = {
            "username": "jojo",
            "password": "oraora",
            "first_name": "Jotaro",
            "last_name": "Kujo",
            "email": "jojo@email.com"
        }

        user = User.objects.create(**user_data)
        cls.user_token = Token.objects.create(user=user)

        admin = User.objects.create_superuser(**admin_data)
        cls.admin_token = Token.objects.create(user=admin)

        another_user = User.objects.create(**another_user_data)
        cls.another_user_token = Token.objects.create(user=another_user)

        cls.base_url = f"/api/users/{user.id}/"
        cls.base_url_error = f"/api/users/1/"

    def test_can_retrieve_a_specific_user(self):
        print("test_can_retrieve_a_specific_user")

        response: Response = self.client.get(self.base_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_if_cannot_found_an_user(self):
        print("test_if_cannot_found_an_user")

        response: Response = self.client.get(self.base_url_error)

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        expected_message = {"detail": "Not found."}
        result_message = response.data

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_message, result_message)

    def test_user_can_update_own_profile(self):
        print("test_user_can_update_own_profile")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response: Response = self.client.patch(self.base_url, data={"last_name": "Garcia"})

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
    
    def test_admin_can_update_random_profiles(self):
        print("test_admin_can_update_random_profiles")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.patch(self.base_url, data={"last_name": "Garcia"})

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_user_cannot_update_profile_from_another_user(self):
        print("test_user_cannot_update_profile_from_another_user")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.another_user_token.key)
        response: Response = self.client.patch(self.base_url, data={"last_name": "Garcia"})

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_cannot_update_is_superuser_field_status(self):
        print("test_cannot_update_is_superuser_field_status")

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response: Response = self.client.patch(self.base_url, data={"is_superuser": True})

        expected_status_field = False
        result_status_field = response.data["is_superuser"]

        self.assertEqual(expected_status_field, result_status_field)