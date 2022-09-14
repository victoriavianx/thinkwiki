from categories.serializers import CreateCategorieSerializer, ListCategorieSerializer
from rest_framework import serializers

from posts.models import Post
from posts.models import Comment

from users.serializers import UserSerializer, UserListCommentSerializer, UserDetailSerializer, UserResumeSerializer


class CommentResumeSerializer(serializers.ModelSerializer):
    user = UserResumeSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "user", "comment", "created_at", "updated_at"]

class PostCreateListSerializer(serializers.ModelSerializer):
    post_collab = UserResumeSerializer(read_only=True, many=True)
    post_likes = UserResumeSerializer(read_only=True, many=True)
    post_comments = CommentResumeSerializer(read_only=True, many=True)
    owner = UserResumeSerializer(read_only=True)
    
    class Meta:
        model = Post
        depth  = 1
        fields = '__all__'
        read_only_fields = ["id", "created_at", "updated_at", "owner", "post_collab", "post_likes"]

   
class PostDetailSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer()
    post_collab = UserResumeSerializer(read_only=True, many=True)
    post_likes = UserResumeSerializer(read_only=True, many=True)
    category = CreateCategorieSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "owner", "post_collab", "post_likes"]
    
class PostUpdateSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer()
    category = CreateCategorieSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["id","title", "content", "created_at", "updated_at","category", "owner"]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class CommentSerializer(serializers.ModelSerializer):
    id_user = UserSerializer(read_only=True)
    id_post = PostCreateListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_user", "id_post", "comment", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CommentListSerializer(serializers.ModelSerializer):
    user = UserListCommentSerializer(read_only=True)
    id_post = PostCreateListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "id_post", "comment", "created_at", "updated_at", "user"]
        read_only_fields = ["id", "created_at", "updated_at"]    

class PostResumeSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    post_collab = UserResumeSerializer(read_only=True, many=True)
    category = CreateCategorieSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'updated_at', 'created_at', 'post_collab', 'category', 'likes']
    
    def get_likes(self, obj):
        return len(obj.post_likes.all())




