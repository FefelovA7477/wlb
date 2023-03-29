from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import TgUserSerializer

import wlb.permissions as custom_permissions


class RetrieveUser(generics.RetrieveAPIView):
    serializer_class = TgUserSerializer

    def get_object(self):
        return self.request.user


# Create your views here.
