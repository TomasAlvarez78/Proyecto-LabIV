from rest_framework import permissions


class CategoryPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        allowed_methods = ['POST', 'PUT', 'PATCH']
        if not request.user.is_autehenticated:
            return False
        if request.user.is_superuser and request.method in allowed_methods:
            return True
