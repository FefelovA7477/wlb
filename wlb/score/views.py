from rest_framework import viewsets

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

# Create your views here.
