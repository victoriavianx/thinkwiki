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
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner or request.user.is_superuser or (request.user in obj.post_collab.all() and request.method == 'PATCH')


class PostCollabAdd(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_superuser

class CollabEditorsListPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_superuser
        