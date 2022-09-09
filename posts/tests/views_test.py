from ast import Delete
from categories.models import Categories
from posts.models import Post

from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase




class PostCreateListViewTest(APITestCase):
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

        
        cls.adm = User.objects.create_superuser(**cls.account_adm)
        cls.category  = {
	        "name":"Filmes"
        }
        cls.category_create = Categories.objects.create(**cls.category)

        cls.post_template = {
            "title": "Teste",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "is_editable":True,
            "category":cls.category_create
        }

        cls.missing_post_template = {}

        cls.base_url = '/api/posts/'
        cls.create_url = '/api/users/'

    def setUp(self) -> None:
        self.common = self.client.post(self.create_url, self.account_common)
        self.common2 = self.client.post(self.create_url, self.account_common2)
        self.user = User.objects.get(id=self.common['id'])
        self.user2 = User.objects.get(id=self.common2['id'])
        token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')

    def test_create_post(self):
        expected_status_code = 201
        expected_return_fields = (
            "id", 
            "title", 
            "content", 
            "is_editable", 
            "created_at", 
            "updated_at", 
            "owner", 
            "category",
            "post_collab",
            'post_likes',
            'post_comments'
        )

        response = self.client.post(self.base_url, self.post_template)

        result_status_code = response.status_code

        self.created_post = response.data

        response_len = len(response.data)

        expected_response_len = len(expected_return_fields)

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(response.data['is_editable'], True)
        self.assertEqual(response.data['owner'], self.common)
        self.assertEqual(response.data['category'], self.category_create)

    def test_fail_create_post(self):
        expected_status_code = 404

        expected_return_fields = (
            "details",   
        )

        response = self.client.post(self.base_url, self.missing_post_template)

        result_status_code = response.status_code

        self.created_post = response.data

        response_len = len(response.data)

        expected_response_len = len(expected_return_fields)

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_post(self):
        expected_status_code = 200
        expected_return_fields = (
            "id", 
            "title", 
            "content", 
            "is_editable", 
            "created_at", 
            "updated_at", 
            "owner", 
            "category",
            "post_collab",
            'post_likes',
            'post_comments'
        )

        response = self.client.get(self.base_url)

        for post in response.data['results']:
            for expected_field in expected_return_fields:
                self.assertIn(expected_field, post)

        result_status_code = response.status_code   
        self.assertEqual(expected_status_code, result_status_code)
        
    def test_list_post_by_category(self):
        expected_status_code = 200
        expected_return_fields = (
            "id", 
            "title", 
            "content", 
            "is_editable", 
            "created_at", 
            "updated_at", 
            "owner", 
            "category",
            "post_collab",
            'post_likes',
            'post_comments'
        )
        category_id = self.category_create.data['id']
        response = self.client.get(f'{self.base_url}categories/{category_id}/')

        for post in response.data['results']:
            for expected_field in expected_return_fields:
                self.assertIn(expected_field, post)

        result_status_code = response.status_code   
        self.assertEqual(expected_status_code, result_status_code)

class RetrieveEditDeleteViewTest(APITestCase):
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
        

        
        cls.adm = User.objects.create_superuser(**cls.account_adm)
        cls.category  = {
	        "name":"Filmes"
        }
        cls.category_create = Categories.objects.create(**cls.category)

        cls.post_template = {
            "title": "Teste",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "is_editable":True,
            "category":cls.category_create
        }
        cls.update_template = {
            "title": "Teste Patch",
        }

        cls.missing_post_template = {}

        cls.base_url = '/api/posts/'
        cls.create_url = '/api/users/'
        
    def setUp(self) -> None:
        self.common = self.client.post(self.create_url, self.account_common)
        self.common2 = self.client.post(self.create_url, self.account_common2)
        self.user = User.objects.get(id=self.common['id'])
        self.user2 = User.objects.get(id=self.common2['id'])
        token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')
        self.post_response = self.client.post(self.base_url, self.post_template)
        self.post_response_delete = self.client.post(self.base_url, self.post_template)
    
    def test_RetrievePostView(self):
        expected_status_code = 200
        expected_return_fields = (
            "id", 
            "title", 
            "content", 
            "is_editable", 
            "created_at", 
            "updated_at", 
            "owner", 
            "category",
            "post_collab",
            'post_likes',
            'post_comments'
        )
        post_id = self.post_response.data['id']
        response = self.client.get(f'{self.base_url + post_id}/')
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)
    
    def test_FailRetrievePostView(self):
        expected_status_code = 400
        expected_return_fields = (
            "details", 
        )
        post_id = "e9361362-8cf0-4ac0-9129-a6f941baOO23"
        response = self.client.get(f'{self.base_url + post_id}/')
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)

    def test_UpdatePostView(self):
        expected_status_code = 200
        expected_return_fields = (
            "id", 
            "title", 
            "content",  
            "created_at", 
            "updated_at", 
            "category",
        )

        post_id = self.post_response.data['id']
        response = self.client.patch(f'{self.base_url + post_id}/', self.update_template)
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)

    def test_DeletePostView(self):
        expected_status_code = 204
        expected_return_fields = ()       

        post_id = self.post_response_delete.data['id']
        response = self.client.delete(f'{self.base_url + post_id}/')
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)
    
    def test_failDeletePostView(self):
        expected_status_code = 403
        expected_return_fields = (
            "details",
        )

        token = Token.objects.get_or_create(user=self.user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')
        

        post_id = self.post_response.data['id']
        response = self.client.delete(f'{self.base_url + post_id}/', self.update_template)
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)
    
    def test_FailUpdatePostView(self):
        expected_status_code = 403
        expected_return_fields = (
            "details",
        )

        token = Token.objects.get_or_create(user=self.user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')

        post_id = self.post_response.data['id']
        response = self.client.patch(f'{self.base_url + post_id}/', self.update_template)
        result_status_code = response.status_code
        response_len = len(response.data)
        expected_response_len = len(expected_return_fields)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)
        
        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(expected_response_len, response_len)

class RetrieveUserViewTest(APITestCase):
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
        

        
        cls.adm = User.objects.create_superuser(**cls.account_adm)
        cls.category  = {
	        "name":"Filmes"
        }
        cls.category_create = Categories.objects.create(**cls.category)

        cls.post_template = {
            "title": "Teste",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "is_editable":True,
            "category":cls.category_create
        }
        cls.update_template = {
            "title": "Teste Patch",
        }

        cls.missing_post_template = {}

        cls.base_url = '/api/posts/'
        cls.create_url = '/api/users/'
        
    def setUp(self) -> None:
        self.common = self.client.post(self.create_url, self.account_common)
        self.common2 = self.client.post(self.create_url, self.account_common2)
        self.user = User.objects.get(id=self.common['id'])
        self.user2 = User.objects.get(id=self.common2['id'])
        token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')
        self.post_response = self.client.post(self.base_url, self.post_template)
        self.post_response_delete = self.client.post(self.base_url, self.post_template)
    
    def test_RetrieveUserPostView(self):
        expected_status_code = 200
        expected_return_fields = (
            "id", 
            "title", 
            "content", 
            "is_editable", 
            "created_at", 
            "updated_at", 
            "owner", 
            "category",
            "post_collab",
            'post_likes',
            'post_comments'
        )
        common_user_id = self.common.data['id']
        response = self.client.get(f'{self.base_url}users/{common_user_id}/')
        result_status_code = response.status_code
        for post in response.data['results']:
            for expected_field in expected_return_fields:
                self.assertIn(expected_field, post)

        result_status_code = response.status_code   
        self.assertEqual(expected_status_code, result_status_code)

    def test_FailRetrieveUserPostView(self):
        expected_status_code = 400
        expected_return_fields = (
            "details", 
        )
        common_user_id = "e9361362-8cf0-4ac0-9129-a6f941baOO23"
        response = self.client.get(f'{self.base_url + common_user_id}/')
        result_status_code = response.status_code
      
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

        result_status_code = response.status_code   
        self.assertEqual(expected_status_code, result_status_code)

class RetrieveUserLikedPostsViewTest(APITestCase):
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
        

        
        cls.adm = User.objects.create_superuser(**cls.account_adm)
        cls.category  = {
	        "name":"Filmes"
        }
        cls.category_create = Categories.objects.create(**cls.category)

        cls.post_template = {
            "title": "Teste",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "is_editable":True,
            "category":cls.category_create
        }
        cls.update_template = {
            "title": "Teste Patch",
        }

        cls.missing_post_template = {}

        cls.base_url = '/api/posts/'
        cls.create_url = '/api/users/'
        
    def setUp(self) -> None:
        self.common = self.client.post(self.create_url, self.account_common)
        self.common2 = self.client.post(self.create_url, self.account_common2)
        self.user = User.objects.get(id=self.common['id'])
        self.user2 = User.objects.get(id=self.common2['id'])
        token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token[0].key}')
        self.post_response = self.client.post(self.base_url, self.post_template)
        self.post_response_delete = self.client.post(self.base_url, self.post_template)

    def test_retrieve_user_liked_posts_view(self):
        ...