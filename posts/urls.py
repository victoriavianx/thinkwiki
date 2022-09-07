from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/str:<id_category>/', views.PostCreateListView.as_view()),
    path('posts/str:<id_post>/str:<id_user>/', views.ContribView.as_view()),
    path('posts/str:<id_post>/', views.PostRetrieveEditDeleteViews.as_view()),
    path('posts/posts/str:<id_user>/', views.ListUserPostsView.as_view()),
    path('api/posts/like/', views.RetrieveUserLikedPosts.as_view()),
    path('api/posts/like/<str:id_post>/', views.UpdateUserLikePost.as_view()),
    path('posts/<id_post>/comments/', views.CommentView.as_view()),
]