from rest_framework import serializers

from categories.models import Categories


class CreateCategorieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = [
            "name",
        ]
        read_only_fields = ["post"]


class ListCategorieSerializer(serializers.ModelSerializer):

        
    class Meta:
        model = Categories
        fields = [
            "name",
        ]
