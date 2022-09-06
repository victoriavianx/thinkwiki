from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:id_post>/comments/', views.CommentView.as_view()),
]