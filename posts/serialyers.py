
from dataclasses import fields
from rest_framework import serializers

from posts.models import Post
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