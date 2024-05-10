from rest_framework import permissions

from .services.tg_authentication import validate_tg_key


class TgOnlyPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        tg_key = request.META.get('HTTP_TG_AUTH_KEY', '')
        return validate_tg_key(tg_key=tg_key)