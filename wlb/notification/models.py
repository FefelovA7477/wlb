from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

def set_default_time() -> datetime.time:
    return datetime.time(hour=0, minute=0)


class Notification(models.Model):
    time = models.TimeField(default=set_default_time)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
# Create your models here.
