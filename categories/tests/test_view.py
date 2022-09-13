
from categories.models import Categories
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import Response, status
from users.models import User


class TestCategoryAuth(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.client: APIClient

        common_user_data = {
            "username": "Robin",
            "email": "Robin@email.com",
            "password": "1234",
            "first_name": "Nico",
            "last_name": "Robin"
        }

        admin_user_data = {
            "username": "Ussop",
            "email": "Ussop@email.com",
            "password": "1234",
            "first_name": "Ussop",
            "last_name": "Sogeking"
        }

        # Criando usuário comum e seu Token
        common_user = User.objects.create_user(**common_user_data)
        cls.common_token = Token.objects.create(user=common_user)

        # Criando usuário admin e seu Token
        admin_user = User.objects.create_superuser(**admin_user_data)
        cls.admin_token = Token.objects.create(user=admin_user)

        cls.category_data_1 = {
            "name": "Manga"
        }

        cls.category_data_3 = {
            "name": "Animes"
        }


        category_data_2 = {
            "name": "Pop"
        }


        category_data_4 = {
            "name": "Filmes"
        }



        category_1 = Categories.objects.create(**category_data_2)

       
        cls.base_category_follow_url = reverse("category-follow-view")
        cls.base_category_url = reverse("category-view")
        cls.base_category_detail_url = reverse("category-detail-view", kwargs={"id_category": category_1.id})
        cls.base_category_follow_detail_url = reverse("category-follow-detail-view", kwargs={"id_category": category_1.id})

    
    def test_common_user_can_add_category(self):
        print("test_common_user_can_add_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.post(
            self.base_category_url, data=self.category_data_3
        )

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_admin_user_can_add_category(self):
        print("test_admin_user_can_add_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.post(
            self.base_category_url, data=self.category_data_3
        )

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_register_category_fields(self):
        print("test_register_category_fields")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.post(self.base_category_url, data=self.category_data_1)
        expected_return_fields = ("id", "name")

        self.assertEqual(len(response.data.keys()), 2)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

        result_return_fields = tuple(response.data.keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)
    

    def test_admin_user_can_add_category_alike(self):
        print("test_admin_user_can_add_category_alike")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.post(
            self.base_category_url, data=self.category_data_1
        )

        response: Response = self.client.post(
            self.base_category_url, data=self.category_data_1
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_common_user_can_list_category(self):
        print("test_common_user_can_list_category")
       
        response: Response = self.client.get(
            self.base_category_url
        )

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_common_user_can_update_category(self):
        print("test_common_user_can_update_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.patch(
            self.base_category_detail_url, data={"name": "Filmes"}
        )

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_admin_user_can_update_category(self):
        print("test_admin_user_can_update_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.patch(
            self.base_category_detail_url, data={"name": "Filmes"}
        )

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_admin_user_can_update_category_alike(self):
        print("test_admin_user_can_update_category_alike")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        
        response: Response = self.client.post(
            self.base_category_url, data=self.category_data_1
        )

        response: Response = self.client.patch(
            self.base_category_detail_url, data={"name": "Manga"}
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_admin_user_update_category_not_exist(self):
        print("test_admin_user_can_update_category_alike")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        categoryID = "87dfe8aa-9868-4497-bcfb-95489339a683"

        response: Response = self.client.patch(
            categoryID, data={"name": "Mangas"}
        )

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_common_user_can_delete_category(self):
        print("test_common_user_can_delete_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.delete(self.base_category_detail_url)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_admin_user_can_delete_category(self):
        print("test_admin_user_can_delete_category")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)
        response: Response = self.client.delete(self.base_category_detail_url)

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_admin_user_delete_category_not_exist(self):
        print("test_admin_user_delete_category_not_exist")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        categoryID = "87dfe8aa-9868-4497-bcfb-95489339a683"

        response: Response = self.client.delete(categoryID)

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_common_user_can_list_category_followed(self):
        print("test_common_user_can_list_category_followed")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
       
        response: Response = self.client.get(
            self.base_category_follow_url
        )

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_unauthenticated_user_can_list_category_followed(self):
        print("test_unauthenticated_user_can_list_category_followed")
       
        response: Response = self.client.get(
            self.base_category_follow_url
        )

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_user_can_followed_categories(self):
        print("test_user_can_followed_categories")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.patch(
            self.base_category_follow_detail_url
        )

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
    

    
    def test_user_can_followed_categories_not_exist(self):
        print("test_user_can_followed_categories_not_exist")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        
        categoryID = "87dfe8aa-9868-4497-bcfb-95489339a683"

        response: Response = self.client.patch(
            categoryID
        )

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    def test_user_can_unfollowed_categories(self):
        print("test_user_can_unfollowed_categories")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.patch(
            self.base_category_follow_detail_url
        )

        response: Response = self.client.patch(
            self.base_category_follow_detail_url
        )

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)


    
    def test_user_can_unfollowed_categories_not_exist(self):
        print("test_user_can_unfollowed_categories")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.common_token.key)
        response: Response = self.client.patch(
            self.base_category_follow_detail_url
        )

        categoryID = "87dfe8aa-9868-4497-bcfb-95489339a683"

        response: Response = self.client.patch(
           categoryID
        )

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
