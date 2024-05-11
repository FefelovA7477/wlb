from rest_framework import viewsets, generics, mixins
from django.utils import timezone

from .serializers import ScoreSerializer
from .permissions import IsCategoryOwner
from . import services as score_services
from backend.permissions import TgOnlyPermissionClass


class ScoreViewset(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    lookup_field = 'id'
    permission_classes = [IsCategoryOwner, TgOnlyPermissionClass]

    def get_queryset(self):
        queryset = score_services.get_all_user_scores(user=self.request.user).order_by('-id')
        return queryset
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except:
            return super().update(request, *args, **kwargs)
    
    def get_object(self):
        category = self.request.data['category']
        if 'date' in self.request.data.keys():
            date = self.request.data['date']
        else:
            date = timezone.now().date()
        return self.get_queryset().filter(category=category, date=date).first()

# Create your views here.
