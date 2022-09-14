
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User
from friendship.models import Friend, FriendshipRequest


class FriendTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user1_data = {
        "username": "user1",
        "first_name": "user",
        "last_name": "1", 
        "email": "user1@mail.com", 
        "password": "1234",
        }

        cls.user2_data = {
        "username": "user2",
        "first_name": "user",
        "last_name": "2", 
        "email": "user2@mail.com", 
        "password": "1234",
        }

        cls.user3_data = {
        "username": "user3",
        "first_name": "user",
        "last_name": "3", 
        "email": "user3@mail.com", 
        "password": "1234",
        }

        cls.user4_data = {
        "username": "user4",
        "first_name": "user",
        "last_name": "4", 
        "email": "user4@mail.com", 
        "password": "1234",
        }

        cls.user5_data = {
        "username": "user5",
        "first_name": "user",
        "last_name": "5", 
        "email": "user5@mail.com", 
        "password": "1234",
        }

        cls.user6_data = {
        "username": "user6",
        "first_name": "user",
        "last_name": "6", 
        "email": "user6@mail.com", 
        "password": "1234",
        }

        cls.user1 = User.objects.create_user(**cls.user1_data)
        cls.user2 = User.objects.create_user(**cls.user2_data)
        cls.user3 = User.objects.create_user(**cls.user3_data)
        cls.user4 = User.objects.create_user(**cls.user4_data)
        cls.user5 = User.objects.create_user(**cls.user5_data)

        cls.user1_token = Token.objects.create(user=cls.user1)
        cls.user2_token = Token.objects.create(user=cls.user2)
        cls.user3_token = Token.objects.create(user=cls.user3)
        cls.user4_token = Token.objects.create(user=cls.user4)
        cls.user5_token = Token.objects.create(user=cls.user5)

        

    def test_model_friend(self):
        Friend.objects.add_friend(from_user=self.user1, to_user=self.user2)

        self.assertEqual(FriendshipRequest.objects.filter(from_user=self.user1).count(), 1)
        self.assertEqual(FriendshipRequest.objects.filter(to_user=self.user2).count(), 1)

        self.assertEqual(len(Friend.objects.requests(self.user1)), 0)
        self.assertEqual(len(Friend.objects.requests(self.user2)), 1)
   
    
    def test_send_friend_request(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user1_token.key)

        response = self.client.post(reverse("send-request", kwargs={"id_friend": self.user2.id}))

        self.assertEqual(response.status_code, 200)

    def test_send_request_user_not_authenticated(self):

        response = self.client.post(reverse("send-request", kwargs={"id_friend": self.user2.id}))

        self.assertEqual(response.status_code, 401)

    def test_send_request_friend_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user1_token.key)
        token_nonexistent = "aae9588b-60d0-4abb-b7fa-d564550503f4"

        response = self.client.post(reverse("send-request", kwargs={"id_friend": token_nonexistent}))

        self.assertEqual(response.status_code, 404)
        
    
    def test_accept_friend_request(self):
        Friend.objects.add_friend(from_user=self.user1, to_user=self.user3)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user3_token.key)

        response = self.client.post(f'/api/users/friends/pending/{self.user1.id}/?accept=1')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Friend.objects.are_friends(self.user1, self.user3), True)

    def test_accept_friend_request_not_authenticated(self):
        Friend.objects.add_friend(from_user=self.user1, to_user=self.user3)

        response = self.client.post(f'/api/users/friends/pending/{self.user3.id}/?accept=1')

        self.assertEqual(response.status_code, 401)

    def test_accept_friend_request_user_not_found(self):
        id_nonexistent = "aae9588b-60d0-4abb-b7fa-d564550503f4"

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user1_token.key)

        response = self.client.post(f'/api/users/friends/pending/{id_nonexistent}/?accept=1')

        self.assertEqual(response.status_code, 404)

    
    def test_reject_friend_request(self):
        Friend.objects.add_friend(from_user=self.user1, to_user=self.user4)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user4_token.key)

        response = self.client.post(f'/api/users/friends/pending/{self.user1.id}/?accept=0')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Friend.objects.are_friends(self.user1, self.user4), False)
        self.assertEqual(Friend.objects.friends(self.user1), [])

    def test_reject_friend_request_not_authenticated(self):
        Friend.objects.add_friend(from_user=self.user1, to_user=self.user4)

        response = self.client.post(f'/api/users/friends/pending/{self.user4.id}/?accept=0')

        self.assertEqual(response.status_code, 401)

    def test_reject_friend_request_user_not_found(self):
        id_nonexistent = "aae9588b-60d0-4abb-b7fa-d564550503f4"

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user1_token.key)

        response = self.client.post(f'/api/users/friends/pending/{id_nonexistent}/?accept=0')

        self.assertEqual(response.status_code, 404)

    
    def test_list_pending_request(self):
         Friend.objects.add_friend(from_user=self.user2, to_user=self.user3)

         self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user3_token.key)

         response = self.client.get(reverse("list-pending-request"))

         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.data.__len__(), 1)

    def test_list_pending_querest(self):
        Friend.objects.add_friend(from_user=self.user2, to_user=self.user3)

        response = self.client.get(reverse("list-friends"))
        
        self.assertEqual(response.status_code, 401)

    
    def test_list_friends_not_authenticated(self):
        Friend.objects.add_friend(from_user=self.user2, to_user=self.user4)

        friend_request = FriendshipRequest.objects.get(from_user=self.user2, to_user=self.user4)
        friend_request.accept()

        response = self.client.get(reverse("list-friends"))
        
        self.assertEqual(response.status_code, 401)

    def test_list_friends(self):
        Friend.objects.add_friend(from_user=self.user2, to_user=self.user5)

        friend_request = FriendshipRequest.objects.get(from_user=self.user2, to_user=self.user5)
        friend_request.accept()

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user2_token.key)

        response = self.client.get(reverse("list-friends"))
  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.__len__(), 1)

    
    def test_delete_friendship(self):
        Friend.objects.add_friend(from_user=self.user3, to_user=self.user4)

        friend_request = FriendshipRequest.objects.get(from_user=self.user3, to_user=self.user4)
        friend_request.accept()

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user3_token.key)

        response = self.client.delete(reverse("send-request", kwargs={"id_friend": self.user4.id}))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Friend.objects.are_friends(self.user3, self.user4), False)
        
    def test_delete_friendship_not_authenticated(self):
        Friend.objects.add_friend(from_user=self.user3, to_user=self.user4)

        friend_request = FriendshipRequest.objects.get(from_user=self.user3, to_user=self.user4)
        friend_request.accept()

        response = self.client.delete(reverse("send-request", kwargs={"id_friend": self.user4.id}))

        self.assertEqual(response.status_code, 401)

    def test_delete_friendship_user_not_found(self):
        id_nonexistent = "aae9588b-60d0-4abb-b7fa-d564550503f4"

        Friend.objects.add_friend(from_user=self.user3, to_user=self.user4)

        friend_request = FriendshipRequest.objects.get(from_user=self.user3, to_user=self.user4)
        friend_request.accept()

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user3_token.key)

        response = self.client.delete(reverse("send-request", kwargs={"id_friend": id_nonexistent}))

        self.assertEqual(response.status_code, 404)
    





 
        

