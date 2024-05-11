from rest_framework import permissions

class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        flag = super().has_object_permission(request, view, obj)
        return flag and obj.user == request.user