from django.urls import path
from . import views

<<<<<<< HEAD

urlpatterns = [
    path('posts/', views.PostCreateListView.as_view()),
    path('posts/str:<id_category>/', views.PostCreateListView.as_view()),
    path('posts/str:<id_post>/', views.PostRetrieveEditDeleteViews.as_view()),
    path('posts/str:<id_post>/str:<id_contributors>/', views.ContribAddRmvView.as_view())
=======
urlpatterns = [
    path('posts/<int:id_post>/comments/', views.CommentView.as_view()),
>>>>>>> 973af516f855b3bd95c36f79cdc33a6b245c1f0f
]