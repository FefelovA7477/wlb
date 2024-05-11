from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from category import services as category_services
from .models import Score


class ScoreShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'score', 'date')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'category', 'score', 'date')
        extra_kwargs = {
            'date': {'required': False},
            'score': {'required': True},
            'category': {'required': True},
            'id': {'read_only': True}
        }