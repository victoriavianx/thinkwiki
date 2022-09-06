from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from users.models import User
from .models import Comment, Post
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from posts.permissions import CollabEditorsListPermission, PostEditPermission, PostSafeMethodsPermission
from posts.serialyers import PostCreateListSerializer

from rest_framework.response import Response

from posts import serializers

# Create your views here.

class PostCreateListView(generics.ListCreateAPIView):

    permission_classes = [PostSafeMethodsPermission]

    serializer_class = PostCreateListSerializer
    

    def get_queryset(self):
        max_users = self.kwargs["num"]
        queryset = Post.objects.all().order_by("-created_at")[0:max_users]
        category = self.request.query_params.get('id_category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PostRetrieveEditDeleteViews(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [PostSafeMethodsPermission, PostEditPermission]

    queryset = Post.objects.all()
    serializer_class = PostCreateListSerializer
    lookup_url_kwarg = "id_post"


    
class ContribAddView(generics.UpdateAPIView):

    permission_classes = [PostSafeMethodsPermission, PostEditPermission]

    queryset = Post.objects.all()
    serializer_class = PostCreateListSerializer
    lookup_url_kwarg = "id_post"

    # def update(self, request, *args, **kwargs):
    #     post_id = self.request.query_params.get('id_post')
    #     contrib_id = self.request.query_params.get('id_contributors')

    #     post = get_object_or_404(Post, id=post_id)
    #     contrib = get_object_or_404(User, id=contrib_id)
        
    #     if contrib not in post.post_collab:
    #         post.post_collab.add(contrib)

    #     serializers = PostCreateListSerializer(post)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()

    #     return Response(serializers.data)

    def perform_update(self, serializer):

        post_id = self.request.query_params.get('id_post')
        contrib_id = self.request.query_params.get('id_contributors')

        post = get_object_or_404(Post, id=post_id)
        contrib = get_object_or_404(User, id=contrib_id)
        
        if contrib not in post.post_collab:
            post.post_collab.add(contrib)
  
        
class ListUserPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateListSerializer
    permission_classes = [PostSafeMethodsPermission]
    def filter_queryset(self, queryset):
        user_id = self.request.query_params.get('id_user')
        user = get_object_or_404(User, id = user_id)
        return queryset.filter(owner = user)


class RetrieveUserLikedPosts(generics.ListAPIView):
    permission_classes = [PostSafeMethodsPermission]
    def get_queryset(self):
        queryset = self.request.user.liked_posts
        return queryset


class UpdateUserLikePost(generics.UpdateAPIView):
    permission_classes = [PostSafeMethodsPermission]
    def perform_update(self, serializer):
        post_id = self.request.query_params.get('id_post')
        post = get_object_or_404(Post, id = post_id)
        user = self.request.user
        
        if user not in post.post_likes:
            post.post_likes.add(user)
        else:
            post.post_likes.remove(user)



class CommentView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["id_post"])

        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["id_post"])

        return Comment.objects.filter(post=post)
