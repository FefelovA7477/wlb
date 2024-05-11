from rest_framework import generics

from .serializers import MetricSerializer


class UpdateMetric(generics.RetrieveUpdateAPIView):
    serializer_class = MetricSerializer

    def get_object(self):
        return self.request.user.metric

# Create your views here.
