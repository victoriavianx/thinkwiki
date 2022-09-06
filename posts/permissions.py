from rest_framework import permissions

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
        