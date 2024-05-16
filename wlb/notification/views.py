from rest_framework import viewsets, generics, mixins
from django.core.exceptions import ObjectDoesNotExist

from .serializers import NotificationSerializer
from .services import filter_notifications
from .permissions import IsOwner
from backend.permissions import TgOnlyPermissionClass


class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [TgOnlyPermissionClass, IsOwner]

    def get_queryset(self):
        return filter_notifications(user=self.request.user)
    

class NotificationCreateRetreiveUpdate(mixins.CreateModelMixin,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       generics.GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [TgOnlyPermissionClass, IsOwner]

    def get_object(self):
        try:
            return self.request.user.notification
        except ObjectDoesNotExist:
            return None
    
    def post(self, request, *args, **kwargs):
        if self.get_object() is None:
            return self.create(request, *args, **kwargs)
        else:
            return self.update(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Create your views here.
