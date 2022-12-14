from django.db import models
import uuid


# Create your models here.


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, )
    title = models.CharField(max_length=60, null=False)
    content = models.TextField(null=False)
    is_editable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    category = models.ForeignKey(
        "categories.Categories", on_delete=models.CASCADE, related_name="posts"
    )
    post_collab = models.ManyToManyField(
        "users.User", related_name="collab_posts"
    )
    post_likes = models.ManyToManyField(
        "users.User", related_name="liked_posts"
    )



class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="post_comments")
    comment = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



