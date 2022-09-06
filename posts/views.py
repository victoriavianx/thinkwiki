from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from posts.models import Post

from posts.permissions import PostSafeMethodsPermission
from posts.serialyers import PostCreateListSerializer

# Create your views here.

class PostCreateListView(ListCreateAPIView):
    authentication_classes =  [TokenAuthentication]
    permission_classes = [PostSafeMethodsPermission]

    serializer_class = PostCreateListSerializer
    

    def get_queryset(self):
        max_users = self.kwargs["num"]
        queryset = Post.objects.all()

        category = self.request.query_params.get('id_category')
        if category is not None:
            queryset = queryset.filter(post__category=category).order_by("-created_at")[0:max_users]
        return queryset




