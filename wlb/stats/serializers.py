from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        exclude = ('user',)