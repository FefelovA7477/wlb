from rest_framework import serializers

from .models import Notification
from . import services as notify_services


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('time', )

    def validate(self, attrs):
        if self.context.get('user', None) is None:
            raise serializers.ValidationError('No user instance provided.')
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context.get('user')
        return notify_services.temp_get_or_create_notification(user=user, **validated_data)