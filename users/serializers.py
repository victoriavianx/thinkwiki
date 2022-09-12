from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

from friendship.models import Friend

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="username already exists")]
    )
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered")]
    )
    
    class Meta:
        model = User
        exclude = ["is_active", "is_staff", "groups", "user_permissions"]
        read_only_fields = ["id", "date_joined", "is_superuser", "last_login"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "posts",
            "user_comments",
            "collab_posts",
            "liked_posts",
            "date_joined",
            "last_login"
        ]
        read_only_fields = [
            "id",
            "is_superuser",
            "posts",
            "user_comments",
            "collab_posts",
            "liked_posts",
            "date_joined",
            "last_login"
        ]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

# Serializers Friend
class ReturnOfPendingRequestsList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]

class PendingRequestsListSerializer(serializers.ModelSerializer):
    user = ReturnOfPendingRequestsList(read_only=True, source="from_user")

    class Meta:
        model = Friend
        fields = ["id", "created", "user"]

class IsActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "posts",
            "user_comments",
            "collab_posts",
            "liked_posts",
            "date_joined",
            "last_login"
        ]
        exclude = ["password"]

    def update(self, instance: User, validated_data: dict) -> User:
        
        for key, value in validated_data.items():
            if key != "is_active":
                continue

            setattr(instance, key, value)

        instance.save()

        return instance

class UserListCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]
        read_only_fields = ["id", "username"]

class UserResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'username']
