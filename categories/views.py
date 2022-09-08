from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from categories.models import Categories
from categories.permissions import IsAdminOrReadOnly
from categories.serializers import (CreateCategorieSerializer,
                                    ListCategorieSerializer)

from .mixins import SerializerByMethodMixin


class ListCreateCategoriesView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsAdminOrReadOnly]

    queryset = Categories.objects.all()

    serializer_map = {
        "GET":  ListCategorieSerializer,
        "POST": CreateCategorieSerializer,
    }

