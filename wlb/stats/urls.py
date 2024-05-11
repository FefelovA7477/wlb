from django.urls import path

from .views import UpdateMetric


urlpatterns = [
    path(r'', UpdateMetric.as_view(), name='Retreive or Update metric'),
]