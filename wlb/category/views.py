from rest_framework import generics

from .serializers import CategorySerializer
from .permissions import IsOwner
from . import services as category_services


class ListCreateCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return category_services.filter_categories(user=self.request.user)
    

class RetrieveUpdateDestroyCategory(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner,]
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return category_services.filter_categories(user=self.request.user)


# Create your views here.
