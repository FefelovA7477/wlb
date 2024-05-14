from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import permissions

from .serializers import NotificationSerializer
from . import services as notify_services

class CRUDNotification(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin):
    """
    На данный момент нотификация только 1, что скорее всего может измениться.

    В данном блоке расписано работа с 1м объектом нотификации (Одиночка).
    """
    
    serializer_class = NotificationSerializer

    def get_object(self):
        try:
            return notify_services.temp_get_notification(user=self.request.user)
        except ObjectDoesNotExist:
            return None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Create your views here.
