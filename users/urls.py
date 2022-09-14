from django.urls import path
from . import views

urlpatterns = [
    path("users/management/", views.UserManagementView.as_view()),
    path("users/friends/", views.ListFriendsView.as_view(), name="list-friends"),
    path("users/friends/pending/", views.ListPendingRequestView.as_view(), name="list-pending-request"),
    path("users/friends/<str:id_friend>/", views.SendFriendRequestAndDeleteFriendshipView.as_view(), name="send-request"),
    path("users/friends/pending/<str:id_friend>/", views.AcceptOrRejectFriendRequestView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/<pk>/", views.UserDetailView.as_view()),
    path("users/management/<pk>/", views.UserManagementDetailView.as_view()),
]
