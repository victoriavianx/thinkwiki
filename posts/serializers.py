from categories.serializers import CreateCategorieSerializer, ListCategorieSerializer
from rest_framework import serializers


from posts.models import Post
from posts.models import Comment
from users.models import User

from users.serializers import UserSerializer, UserListCommentSerializer, UserDetailSerializer, UserResumeSerializer


class CommentResumeSerializer(serializers.ModelSerializer):
    user = UserResumeSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "user", "comment", "created_at", "updated_at"]

class CommentResume(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment", "user"]
        read_only_fields = ["id", "comment", "user"] 

class PostCreateSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Post
        depth  = 1
        fields = ["id","title",  "content", "is_editable", "created_at", "updated_at", "category"]
        read_only_fields = ["id", "created_at", "updated_at", "owner"]

class PostSerializer(serializers.ModelSerializer):
    post_collab = UserResumeSerializer(read_only=True, many=True)
    post_likes = UserResumeSerializer(read_only=True, many=True)
    post_comments = CommentResume(read_only=True, many=True)
    owner = UserResumeSerializer(read_only=True)
        
    class Meta:
        model = Post
        depth  = 1
        fields = '__all__'
        read_only_fields = ["id", "created_at", "updated_at", "owner", "post_collab", "post_likes"]
   
class PostDetailSerializer(serializers.ModelSerializer):
    owner = UserResumeSerializer()
    post_collab = UserResumeSerializer(read_only=True, many=True)
    post_likes = UserResumeSerializer(read_only=True, many=True)
    category = CreateCategorieSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "owner", "post_collab", "post_likes"]
    
class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "content", "created_at", "updated_at","category"]
        read_only_fields = ["id", "created_at", "updated_at"]

        
class CommentSerializer(serializers.ModelSerializer):
    id_user = UserSerializer(read_only=True)
    id_post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_user", "id_post", "comment", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CommentListSerializer(serializers.ModelSerializer):
    user = UserListCommentSerializer(read_only=True)
    id_post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_post", "comment", "created_at", "updated_at", "user"]
        read_only_fields = ["id", "created_at", "updated_at"]    

class PostResumeSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    category = CreateCategorieSerializer(read_only=True)
    owner = UserResumeSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'updated_at', 'created_at', 'category', 'likes', 'owner']
    
    def get_likes(self, obj):
        return len(obj.post_likes.all())

class UserMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


