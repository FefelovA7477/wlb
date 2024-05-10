from rest_framework import viewsets

from .serializers import ScoreSerializer
from .permissions import IsCategoryOwner
from . import services as score_services


class ScoreViewset(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    permission_classes = [IsCategoryOwner,]
    lookup_field = 'id'

    def get_queryset(self):
        queryset = score_services.get_all_user_scores(user=self.request.user).order_by('-id')
        return queryset

# Create your views here.
