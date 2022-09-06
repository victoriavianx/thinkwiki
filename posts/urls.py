from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/str:<id_category>/', views.PostCreateListView.as_view())
]