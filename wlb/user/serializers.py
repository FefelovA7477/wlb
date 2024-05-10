from rest_framework import serializers
from django.contrib.auth import get_user_model

from category.serializers import ShortCategorySerializer
from .services import create_user

User = get_user_model()

class TgUserSerializer(serializers.ModelSerializer):
    categories = ShortCategorySerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'is_new', 'first_name', 'tg_chat_id', 'categories')
        extra_kwargs = {'categories': {'read_only': True}}

    def create(self, validated_data):
        return create_user(**validated_data)