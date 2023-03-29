from rest_framework import serializers
from django.utils import timezone

from .models import Category
from . import services as category_services
from score.serializers import ScoreSerializer
from score import services as score_services

class CategorySerializer(serializers.ModelSerializer):
    scores = serializers.SerializerMethodField(read_only=True)

    def get_scores(self, obj):
        curr_time = timezone.now()
        scores = score_services.filter_scores(
            category=obj,
            date__lte=curr_time,
            date__gte=curr_time-timezone.timedelta(days=7)
        )
        serializer = ScoreSerializer(instance=scores, many=True)
        # if serializer.is_valid():
        return serializer.data
        # raise serializers.ValidationError('Some problems with serializing scores.')

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'is_active', 'scores')
        extra_kwargs = {
            'description': {'required': False},
            'id': {'read_only': True}
        }

    def validate(self, attrs):
        if self.context.get('user', None) is None:
            raise serializers.ValidationError('No tg_user instance.')
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context.get('user')
        category = category_services.create_category(user=user, **validated_data)
        return category


class ShortCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id', 'is_active')
        extra_kwargs = {'name': {'read_only': True}}