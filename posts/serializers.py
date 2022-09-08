from rest_framework import serializers

from posts.models import Post
from .models import Comment

from users.serializers import UserSerializer

class PostCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "owner", "post_collab", "post_likes"]
    

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "id_post", "comment", "created_at", "updated_at"]
        read_only_fields = ["id_post"]