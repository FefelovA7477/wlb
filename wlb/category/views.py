from rest_framework import viewsets

from .serializers import CategorySerializer
from .permissions import IsOwner
from . import services as category_services
from backend.permissions import TgOnlyPermissionClass


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = 'id'
    permission_classes = [IsOwner, TgOnlyPermissionClass]

    def get_queryset(self):
        return category_services.filter_categories(user=self.request.user).order_by('id')


# Create your views here.
