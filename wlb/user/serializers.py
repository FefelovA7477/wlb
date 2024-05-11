from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model

from category.serializers import ShortCategorySerializer
from stats.serializers import MetricSerializer
from .services import create_user

User = get_user_model()

class TgUserSerializer(serializers.ModelSerializer):
    categories = ShortCategorySerializer(many=True, read_only=True)
    metric = MetricSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('is_new', 'first_name', 'tg_chat_id', 'categories', 'metric')

    def create(self, validated_data):
        username = validated_data['tg_chat_id']
        try:
            return create_user(username=username, **validated_data)
        except:
            raise ValidationError({'details': 'User with provided username already exists.'})