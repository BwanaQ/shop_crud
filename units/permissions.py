from rest_framework.permissions import BasePermission, SAFE_METHODS


class UnitWritePermission(BasePermission):
    message = 'Rights restricted to unit creator only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
