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
        read_only_fields = ["id", "date_joined", "is_superuser", "is_active", "last_login"]
        exclude = ["is_staff", "groups", "user_permissions"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    # Aqui vou colocar os serializers dos apps relacionados com o user

    class Meta:
        model = User
        # Está faltando os campos de "categorias seguidas" e "amigos" porque as models não estão feitas e não sei como vai ser o nome das related_names
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "posts",
            "comments_posts",
            "collab_posts",
            "liked_posts",
            "date_joined",
            "last_login"
        ]
        read_only_fields = [
            "id",
            "is_superuser",
            "posts",
            "comments_posts",
            "collab_posts",
            "liked_posts",
            "date_joined",
            "last_login"
        ]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    # email = serializers.EmailField(write_only=True)
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

