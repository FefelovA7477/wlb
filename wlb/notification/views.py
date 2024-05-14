from rest_framework import viewsets

from .serializers import NotificationSerializer
from .services import filter_notifications
from .permissions import IsOwner
from backend.permissions import TgOnlyPermissionClass


class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [TgOnlyPermissionClass, IsOwner]

    def get_queryset(self):
        return filter_notifications(user=self.request.user)

# Create your views here.
