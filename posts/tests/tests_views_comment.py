from email.policy import HTTP
from unittest import result
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from posts.models import Post, Comment
from categories.models import Categories

class CommentViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.owner_user = {
            "username": "testOwner",
            "email": "testOwner@email.com",
            "first_name": "Teste",
            "last_name": "Owner",
            "password": "1234"
            }
        owner = User.objects.create_user(**cls.owner_user)
        cls.owner_token = Token.objects.create(user=owner)

        cls.admin_user = {
            "username": "testAdmin",
            "email": "testAdmin@email.com",
            "first_name": "Teste",
            "last_name": "Admin",
            "password": "1234"
            }
        admin = User.objects.create_superuser(**cls.admin_user)
        cls.admin_token = Token.objects.create(user=admin)

        cls.other_user = {
            "username": "testOther",
            "email": "testOther@email.com",
            "first_name": "Teste",
            "last_name": "Other",
            "password": "1234"
            }
        other = User.objects.create_user(**cls.other_user)
        cls.other_user_token = Token.objects.create(user=other)

        category  = {"name":"Jogos"}
        cls.category_test = Categories.objects.create(**category)

        post_test = {
            "title": "Teste",
            "content": "testando",
            "is_editable":True,
            "category":cls.category_test,
            "owner":owner
        }
        post = Post.objects.create(**post_test)

        cls.new_comment = {"comment": "this is a cool comment TEST!"}
        cls.comment_test = Comment.objects.create(
            **cls.new_comment,
            user = owner,
            post = post,
        )

        cls.base_url = f"/api/posts/{post.id}/comments/"
        cls.base_detail_url = f"/api/posts/{post.id}/comments/{cls.comment_test.id}/"
        cls.base_detail_url_fail = f"/api/posts/{post.id}/comments/404/"

    def test_creat_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.owner_token.key)

        response = self.client.post(self.base_url, data=self.new_comment, format="json")

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_creat_comment_unauthorized(self):

        response = self.client.post(self.base_url, data=self.new_comment, format="json")

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_list_comment(self):

        response = self.client.get(self.base_url, format="json")

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_owner_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.owner_token.key)

        response = self.client.patch(self.base_detail_url, data={"comment": "testei"}, format="json")

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_admin_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        response = self.client.patch(self.base_detail_url, data={"comment": "testado"}, format="json")

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_comment_forbidden(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.other_user_token.key)

        response = self.client.patch(self.base_detail_url, data={"comment": "não posso testar"}, format="json")

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_comment_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.owner_token.key)

        response = self.client.patch(self.base_detail_url_fail, data={"comment": "testei"}, format="json")

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_delete_owner_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.owner_token.key)

        response = self.client.delete(self.base_detail_url, format="json")

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_delete_admin_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token.key)

        response = self.client.delete(self.base_detail_url, format="json")

        expected_status_code = status.HTTP_204_NO_CONTENT
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_delete_comment_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.owner_token.key)

        response = self.client.delete(self.base_detail_url_fail, format="json")

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_delete_comment_forbidden(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.other_user_token.key)

        response = self.client.delete(self.base_detail_url, format="json")

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
