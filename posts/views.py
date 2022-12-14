from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import Response, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from utils.mixins import SerializerByMethodMixin

from users.models import User
from posts.models import Comment, Post
from categories.models import Categories

from posts.serializers import CommentListSerializer, CommentSerializer, PostCreateSerializer, PostDetailSerializer, PostResumeSerializer, PostSerializer, PostUpdateSerializer

from posts.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, LikePermissions, PostEditPermission, PostSafeMethodsPermission, PostCollabAdd



from rest_framework.response import Response
from posts.email.notification import Send_notification
from rest_framework.exceptions import ValidationError



# Create your views here.

class PostCreateListView(SerializerByMethodMixin,generics.ListCreateAPIView):

    permission_classes = [PostSafeMethodsPermission]
    queryset = Post.objects.all()
    serializer_map = {
        "GET":PostResumeSerializer,
        "POST":PostCreateSerializer
        } 

    def perform_create(self, serializer):
        if not self.request.data['category']:
            raise ValidationError
        category = get_object_or_404(Categories, id = self.request.data['category'])  
        Send_notification.friend_notification(self.request.user.id)      
        return serializer.save(owner = self.request.user, category=category)




class ListByCategoryView(generics.ListAPIView):
    permission_classes = [PostSafeMethodsPermission]

    serializer_class = PostResumeSerializer

    lookup_url_kwarg = "id_category"

    def get_queryset(self):
        category_id = self.kwargs.get('id_category')
        queryset = Post.objects.all()
        if category_id is not None:
            queryset = queryset.filter(category = category_id)
        return queryset


class PostRetrieveEditDeleteViews(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostEditPermission]
    serializer_map ={
        "GET": PostDetailSerializer,
        "POST":PostResumeSerializer,
        "PATCH":PostUpdateSerializer,
        "DELETE": PostCreateSerializer,
    }
    queryset = Post.objects.all()
   
    lookup_url_kwarg = "id_post"

    def update(self, request, *args, **kwargs):
        

        return super().update(request, *args, **kwargs)

    

    
class ContribView(generics.UpdateAPIView):
    permission_classes = [PostSafeMethodsPermission, PostCollabAdd]

    queryset = Post.objects.all()
    serializer_class = PostResumeSerializer
    lookup_url_kwarg = "id_post"

    def perform_update(self, serializer):
        
        post_id = self.kwargs.get('id_post')
        contrib_id = self.kwargs.get('id_user')

        post = get_object_or_404(Post, id=post_id)
        contrib = get_object_or_404(User, id=contrib_id)
        
        if contrib not in post.post_collab.all():
            post.post_collab.add(contrib)
        else:
            post.post_collab.remove(contrib)
  
        
class ListUserPostsView(generics.ListAPIView):
    permission_classes = [PostSafeMethodsPermission]
    queryset = Post.objects.all()
    serializer_class = PostResumeSerializer

    def filter_queryset(self, queryset):
       
        user_id = self.kwargs.get('id_user')
        user = get_object_or_404(User, id = user_id)
        return queryset.filter(owner = user)


class RetrieveUserLikedPosts(generics.ListAPIView):
    permission_classes = [LikePermissions]
    serializer_class = PostResumeSerializer
    def get_queryset(self):
        queryset = self.request.user.liked_posts.all()
        return queryset


class UpdateUserLikePost(generics.UpdateAPIView):
    permission_classes = [PostSafeMethodsPermission]
    queryset = Post.objects.all()
    lookup_url_kwarg = "id_post"
    serializer_class = PostDetailSerializer

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        post_id = self.kwargs.get('id_post')
        post = get_object_or_404(Post, id = post_id)
        user = self.request.user
        
        if user not in post.post_likes.all():
            post.post_likes.add(user)
        else:
            post.post_likes.remove(user)



class CommentView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_map = {
        "GET": CommentListSerializer,
        "POST": CommentSerializer,
    }

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["id_post"])

        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["id_post"])

        return Comment.objects.filter(post=post).order_by("-created_at")


class CommentDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly | IsOwnerOrReadOnly]

    queryset = Comment.objects.all()
    lookup_url_kwarg = "id_post" and "id_comment"

    serializer_map = {
        "GET": CommentListSerializer,
        "PATCH": CommentSerializer,
        "DELETE": CommentSerializer,
    }
