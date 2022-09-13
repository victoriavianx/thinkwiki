from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.ListCreateCategoriesView.as_view()),
    path("categories/", views.ListCreateCategoriesView.as_view(), name="category-view"),
    path("categories/<str:id_category>/", views.ListDetailViews.as_view(), name="category-detail-view"),
    path("categories/follow/<str:id_category>/", views.UpdateUserCategoryFollowed.as_view())
]
