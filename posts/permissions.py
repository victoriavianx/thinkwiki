from rest_framework import permissions

class PostSafeMethodsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous == True:
            return False
        return request.user.is_authenticated
        