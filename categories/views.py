from django.shortcuts import get_object_or_404
from posts.models import Post
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from categories.models import Categories
from categories.permissions import IsAdminOrReadOnly, IsOwner
from categories.serializers import (CreateCategorieSerializer,
                                    ListCategorieSerializer,
                                    ListDetailCategoireSereliazer,
                                    UpdateCategorieSerializer)

from .mixins import SerializerByMethodMixin


class ListCreateCategoriesView(SerializerByMethodMixin, generics.ListCreateAPIView):

    permission_classes = [IsAdminOrReadOnly]

    queryset = Categories.objects.all()

    serializer_map = {
        "GET":  ListCategorieSerializer,
        "POST": CreateCategorieSerializer,
    }


class ListDetailViews(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAdminOrReadOnly]
    

    serializer_class = ListDetailCategoireSereliazer
    queryset = Categories.objects.all()

    serializer_map = {
        "GET":  ListDetailCategoireSereliazer,
        "PATCH": UpdateCategorieSerializer,
    }
    
    lookup_url_kwarg = "id_category"


class RetrieveUserCategoryFollowed(generics.ListAPIView):
    permission_classes = [IsOwner]
    def get_queryset(self):
        queryset = self.request.user.followed_categories
        # ipdb.set_trace()
        return queryset


class UpdateUserCategoryFollowed(generics.UpdateAPIView):
    permission_classes = [IsOwner]

    lookup_url_kwarg = "id_category"

    def perform_update(self, serializer):
        category_id = self.kwargs.get("id_category")
        category = get_object_or_404(Categories, id = category_id)
        user = self.request.user
        
        if user not in  category.categories_followed:
            category.categories_followed.add(user)
        else:
            category.categories_followed.remove(user)

   
