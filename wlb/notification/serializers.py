from rest_framework import serializers

from .models import Notification
from . import services as notify_services


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('time', )

    def create(self, validated_data):
        user = self.context['request'].user
        return notify_services.create_notification(user=user, **validated_data)