from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_new = models.BooleanField(default=True)
    tg_chat_id = models.CharField(max_length=256, unique=True)
    utm = models.CharField(max_length=256, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

# Create your models here.
