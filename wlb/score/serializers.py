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
    category_id = serializers.IntegerField()

    class Meta:
        model = Score
        fields = ('category_id', 'score', 'date')
        extra_kwargs = {
            'date': {'required': False},
            'score': {'required': True},
            'category_id': {'required': True},
        }

    def validate(self, attrs):
        try:
            category_services.get_category(id=attrs['category_id'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError(f'No category instance with provided id. {id}')
        except KeyError:
            raise serializers.ValidationError(f'Wrong provided structure.')
        except Exception as e:
            raise serializers.ValidationError(e)
        return super().validate(attrs)
        
    def create(self, validated_data):
        category_object = category_services.get_category(id=validated_data['category_id'])
        score = score_services.create_score_object(
            score=validated_data['score'],
            category=category_object
        )
        return score