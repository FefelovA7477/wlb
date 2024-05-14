from rest_framework.permissions import IsAuthenticated


class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        flag = super().has_object_permission(request, view, obj)
        return flag and self.request.user == obj.user