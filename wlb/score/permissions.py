from rest_framework import permissions

class IsCategoryOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        flag = super().has_object_permission(request, view, obj)
        return flag and request.user == obj.category.user