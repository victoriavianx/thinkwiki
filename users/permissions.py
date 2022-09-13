from rest_framework import permissions

class IsAdminOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or obj == request.user

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        return request.user.is_superuser or obj == request.user