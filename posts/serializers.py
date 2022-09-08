from rest_framework import serializers

from posts.models import Post
from .models import Comment

from users.serializers import UserSerializer, UserListCommentSerializer

class PostCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    id_user = UserSerializer(read_only=True)
    id_post = PostCreateListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_user", "id_post", "comment", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CommentListSerializer(serializers.ModelSerializer):
    user = UserListCommentSerializer(read_only=True)
    id_post = PostCreateListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_post", "comment", "created_at", "updated_at", "user"]
        read_only_fields = ["id", "created_at", "updated_at"]
