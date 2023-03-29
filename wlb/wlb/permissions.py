from rest_framework import permissions


class TgOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user \
                and request.user.is_authenticated \
                and request.user.username == 'tg_bot'
    

class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user \
                and request.user.is_authenticated \
                and request.user == obj.user
    

class IsAllowedToScoreCategory(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user \
                and request.user.is_authenticated \
                and request.user == request.data.get('category').user
        except Exception as e:
            return False