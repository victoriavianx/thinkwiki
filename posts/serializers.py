from rest_framework import serializers

from .models import Comment

from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "id_post", "comment", "created_at", "updated_at"]
        read_only_fields = ["id_post"]