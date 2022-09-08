from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = (
    path("users/", views.UserView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/<pk>/", views.UserDetailView.as_view()),
    path("users/<pk>/management/", views.UserManagementView.as_view())
)