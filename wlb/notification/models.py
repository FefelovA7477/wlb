from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
import datetime

from utils.utc_time import get_time_with_default_utc

User = get_user_model()

def set_default_time() -> datetime.time:
    return datetime.time(hour=0, minute=0)


class Notification(models.Model):
    time = models.TimeField(default=set_default_time)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='notification'
    )

    def save(self, *args, **kwargs) -> None:
        self.time = get_time_with_default_utc(self.time)
        return super().save(*args, **kwargs)
# Create your models here.
