from django.test import TestCase

from categories.models import Categories
from posts.models import Post, Comment
from users.models import User

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = {
            "username": "testOwner",
            "email": "testOwner@email.com",
            "first_name": "Teste",
            "last_name": "Owner",
            "password": "1234"
            }
        cls.owner = User.objects.create_user(**user)

        category  = {"name":"Jogos"}
        cls.category_test = Categories.objects.create(**category)

        post_test = {
            "title": "Teste",
            "content": "testando",
            "is_editable":True,
            "category":cls.category_test,
            "owner":cls.owner
        }
        cls.post = Post.objects.create(**post_test)

        # cls.new_comment = "this is a cool comment TEST! :)"
        cls.new_comment = "this is a cool comment TEST!"
        cls.comment_test = Comment.objects.create(
            comment = cls.new_comment,
            user = cls.owner,
            post = cls.post,
        )

    def test_comment_fields(self):
        self.assertEqual(self.comment_test.comment, self.new_comment)
        self.assertEqual(self.comment_test.user, self.owner)
        self.assertEqual(self.comment_test.post, self.post)
