from rest_framework import serializers
from django.utils import timezone

from .models import Category
from . import services as category_services
from score.serializers import ScoreSerializer
from score import services as score_services
from backend.services.cmn_services import filter_objects

class CategorySerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'is_active', 'scores', 'priority', 'color')
        extra_kwargs = {
            'description': {'required': False},
            'id': {'read_only': True},
            'scores': {'read_only': True}
        }

    def create(self, validated_data):
        user =  self.context['request'].user
        category = category_services.create_category(user=user, **validated_data)
        return category


class ShortCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id', 'is_active')
        extra_kwargs = {'name': {'read_only': True}}