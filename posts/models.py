from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=60, null=False)
    content = models.TextField(null=False)
    is_editable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    post_collab = models.ManyToManyField(
        "users.User", related_name="collab_posts"
    )
    post_likes = models.ManyToManyField(
        "users.User", related_name="liked_posts"
    )
    post_comments = models.ManyToManyField(
        "users.User",
        through="posts.Comments",
        related_name="comments_posts"
    )


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
