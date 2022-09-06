from rest_framework import permissions
from rest_framework.views import View, Request

from .models import Comment

class PostSafeMethodsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous == True:
            return False
        return request.user.is_authenticated

class PostEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user == obj.owner | request.user.is_superuser | (request.user in obj.post_collab and request.method == 'PATCH')

class CollabEditorsListPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner | request.user.is_superuser


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request:Request, view: View, obj: Comment) -> bool:
        return request.method in permissions.SAFE_METHODS or (request.user == obj.user | request.user.is_superuser)