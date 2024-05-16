from rest_framework import generics, mixins
from django.utils import timezone

from .serializers import ScoreSerializer
from .permissions import IsCategoryOwner
from . import services as score_services
from backend.permissions import TgOnlyPermissionClass


class ScoreCRUD(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    serializer_class = ScoreSerializer
    lookup_field = 'id'
    permission_classes = [IsCategoryOwner, TgOnlyPermissionClass]

    def get_queryset(self):
        queryset = score_services.get_all_user_scores(user=self.request.user).order_by('-id')
        return queryset
    
    def post(self, request, *args, **kwargs):
        if self.get_object() is None:
            return self.create(request, *args, **kwargs)
        else:
            return self.update(request, *args, **kwargs)
        
    def get(self, request, *args, **kwrags):
        return self.list(request, *args, **kwrags)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get_object(self):
        category = self.request.data['category']
        if 'date' in self.request.data.keys():
            date = self.request.data['date']
        else:
            date = timezone.now().date()
        return self.get_queryset().filter(category=category, date=date).first()

# Create your views here.
