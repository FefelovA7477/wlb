from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from .serializers import CategorySerializer
from . import services as category_services
import wlb.permissions as custom_permissions


class ListCreateCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context
    
    def get_queryset(self):
        return category_services.filter_categories(user=self.request.user)
    

class RetrieveUpdateDestroyCategory(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return category_services.filter_categories(user=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context


# Create your views here.
