from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/categories/<str:id_category>/', views.PostCreateListView.as_view()),
    path('posts/users/<str:id_user>/', views.ListUserPostsView.as_view()),
    path('posts/like/', views.RetrieveUserLikedPosts.as_view()),
    path('posts/like/<str:id_post>/', views.UpdateUserLikePost.as_view()),
    path('posts/<str:id_post>/<str:id_user>/', views.ContribView.as_view()),
    path('comments/posts/<str:id_post>/', views.CommentView.as_view()),
    path('comments/<str:id_comment>/posts/<str:id_post>/', views.CommentDetailView.as_view()),
    path('posts/<str:id_post>/', views.PostRetrieveEditDeleteViews.as_view()),
]
