from posts.serialyers import PostDetailSerializer
from rest_framework import serializers
from rest_framework.exceptions import APIException

from categories.models import Categories


class UniqueValidationError(APIException):
    ...

class CreateCategorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = [
            "name",
        ]

    def validate_unique_name(self, value: str):
        if Categories.objects.filter(name=value).exists():

            raise UniqueValidationError()

        return value


class ListCategorieSerializer(serializers.ModelSerializer):

        
    class Meta:
        model = Categories
        fields = [
            "name",
        ]


class ListDetailCategoireSereliazer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = [
            "name",
            "posts"
        ]

    posts = PostDetailSerializer(read_only=True, many = True)
