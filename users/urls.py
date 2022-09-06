from django.urls import path

from . import views

urls_patterns = (
    path("users/", views.UserView.as_view()),
    path("users/login/", views.LoginView.as_view())
)