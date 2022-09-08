from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/categories/<id_category>/', views.PostCreateListView.as_view()),
    path('posts/<id_post>/<id_user>/', views.ContribView.as_view()),
    path('posts/<id_post>/', views.PostRetrieveEditDeleteViews.as_view()),
    path('posts/users/<id_user>/', views.ListUserPostsView.as_view()),
    path('posts/<id_post>/comments/', views.CommentView.as_view()),
    path('posts/like/', views.RetrieveUserLikedPosts.as_view()),
    path('posts/like/<id_post>/', views.UpdateUserLikePost.as_view()),
]