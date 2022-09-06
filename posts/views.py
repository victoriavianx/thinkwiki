from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from posts.models import Post

from posts.permissions import CollabEditorsListPermission, PostEditPermission, PostSafeMethodsPermission
from posts.serialyers import PostCreateListSerializer

# Create your views here.

class PostCreateListView(generics.ListCreateAPIView):
    authentication_classes =  [TokenAuthentication]
    permission_classes = [PostSafeMethodsPermission]

    serializer_class = PostCreateListSerializer
    

    def get_queryset(self):
        max_users = self.kwargs["num"]
        queryset = Post.objects.all().order_by("-created_at")[0:max_users]
        category = self.request.query_params.get('id_category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class PostRetrieveEditDeleteViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostSafeMethodsPermission, PostEditPermission]

    serializer_class = PostCreateListSerializer

    queryset = Post.objects.all()

    def get_queryset(self):
        post_id = self.request.query_params.get('id_post')
        queryset = self.queryset.get(id=post_id)

        return queryset

class ContribAddRmvView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostSafeMethodsPermission, CollabEditorsListPermission]

    queryset = Post.objects.all()

    def get_queryset(self):
        post_id = self.request.query_params.get('id_post')
        contrib_id = self.request.query_params.get('id_contributors')

        queryset = self.queryset.get(id=post_id)

        return queryset



