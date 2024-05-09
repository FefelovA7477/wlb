from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.serializers import ValidationError
from django.db.utils import IntegrityError

from .serializers import ScoreSerializer
from . import services as score_services
import wlb.permissions as custom_permissions


class ListCreateScore(generics.CreateAPIView):
    serializer_class = ScoreSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        queryset = score_services.get_all_user_scores(user=self.request.user).order_by('-id')
        return queryset
    
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                data={'details': 'Нарушение ограничения уникальности (date, category)'},
                status=status.HTTP_409_CONFLICT
            )
        except ValidationError as e:
            return Response(data=e.get_full_details(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                data=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RetrieveUpdateDestroyScore(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScoreSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        queryset = score_services.get_all_user_scores(user=self.request.user).order_by('-id')
        return queryset

# Create your views here.
