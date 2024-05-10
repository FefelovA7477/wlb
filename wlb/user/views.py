from rest_framework import viewsets, mixins

from .serializers import TgUserSerializer
from backend.permissions import TgOnlyPermissionClass

class CreateRetrieveUser(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = TgUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [TgOnlyPermissionClass,]
        return super().get_permissions()
    
    def get_object(self):
        return self.request.user



# Create your views here.
