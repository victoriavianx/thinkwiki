from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = (
    path("users/", views.UserView.as_view()),
    path("users/login/", ObtainAuthToken.as_view())
)