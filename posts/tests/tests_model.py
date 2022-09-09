from django.test import TestCase
from categories.models import Categories
from posts.models import Post

from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_adm = {
            "username": "teste adm",
            "email": "testeAdm@mail.com",
            "first_name": "Teste",
            "last_name": "Adm",
            "password": "1234",
        }

        cls.account_common = {
            "username": "teste comum",
            "email": "testeComum@mail.com",
            "first_name": "Teste",
            "last_name": "Comum",
            "password": "1234",
        }

        cls.account_common2 = {
            "username": "teste comum2",
            "email": "testeComum2@mail.com",
            "first_name": "Teste",
            "last_name": "Comum2",
            "password": "1234",
        }

        cls.common = User.objects.create_user(**cls.account_common)
        cls.common2 = User.objects.create_user(**cls.account_common2)
        cls.adm = User.objects.create_superuser(**cls.account_adm)
        cls.category  = {
	        "name":"Filmes"
        }
        cls.category_create = Categories.objects.create(**cls.category)

        cls.post_template = {
            "title": "Teste",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "is_editable":True,
            "category":cls.category_create,
            "owner":cls.common
        }

        cls.post = Post.objects.create(**cls.post_template)
   

    def test_post_fields(self):
        self.assertEqual(self.post_template['title'], self.post.title)
        self.assertEqual(self.post_template['content'], self.post.content)
        self.assertEqual(self.post_template['is_editable'], self.post.is_editable)
        self.assertEqual(self.post_template['category'], self.post.category)


    def test_post_title_length(self):
        post = Post.objects.get(id = self.post.id)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 60)

