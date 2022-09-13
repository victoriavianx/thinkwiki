from django.shortcuts import get_object_or_404
from posts.models import Post
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from categories.mixins import SerializerByMethodMixin
from categories.models import Categories
from categories.permissions import IsAdminOrReadOnly, IsOwner
from categories.serializers import (CategoriesFollowedSerializer,
                                    CreateCategorieSerializer,
                                    ListCategorieSerializer,
                                    ListDetailCategoireSereliazer,
                                    UpdateCategorieSerializer)


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



class RetrieveUserCategoryFollowed(SerializerByMethodMixin,generics.ListAPIView):
    permission_classes = [IsOwner]

    serializer_map = {
        "GET":  CategoriesFollowedSerializer
    }
    
    def get_queryset(self):
        queryset = self.request.user.followed_categories.all()
        # ipdb.set_trace()
        return queryset



class UpdateUserCategoryFollowed(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,IsOwner]

    queryset = Categories.objects.all()

    lookup_url_kwarg = "id_category"

    serializer_class = CategoriesFollowedSerializer

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        category_id = self.kwargs.get("id_category")
        category = get_object_or_404(Categories, id = category_id)
        user = self.request.user
        
        if user not in  category.categories_followed.all():
            category.categories_followed.add(user)
        else:
            category.categories_followed.remove(user)


   
