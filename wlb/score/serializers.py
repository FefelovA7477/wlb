from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from category import services as category_services
from .models import Score
from . import services as score_services


class ScoreShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('score', 'date')


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
        
    def create(self, validated_data):
        category_object = validated_data['category']
        user = self.context.get('user', None)
        if user != category_object.user:
            raise serializers.ValidationError(f'User has no permissions to create score in this category!')
        score = score_services.create_score_object(
            score=validated_data['score'],
            category=category_object
        )
        return score
    
    def update(self, instance, validated_data):
        try:
            score = validated_data['score']
            instance.score = score
            instance.save()
            return instance
        except Exception as e:
            return instance