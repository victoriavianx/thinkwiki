from rest_framework import serializers
from rest_framework.exceptions import APIException

from categories.models import Categories


class UniqueValidationError(APIException):
    ...

class CreateCategorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = [
           "id", "name"
        ]
        read_only_fields = ["id"]

    def validate_unique_name(self, value: str):
        if Categories.objects.filter(name=value).exists():

            raise UniqueValidationError()

        return value


class ListCategorieSerializer(serializers.ModelSerializer):

        
    class Meta:
        model = Categories
        fields = [
            "id",
            "name",
        ]
    


class ListDetailCategoireSereliazer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = [
            "id",
            "name",
        ]

class UpdateCategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ["id", "name"]

class CategoriesFollowedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = [
            "id",
            "name"
        ]
