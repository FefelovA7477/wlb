from django.db import models
from django.contrib.auth import get_user_model
from typing import List

User = get_user_model()


class CategoryManager(models.Manager):
    def clone_default_categories(self) -> List[object | None]:
        default_categories = self.get_queryset().filter(is_default=True)
        cloned_default_categories = [category.copy() for category in default_categories]
        return cloned_default_categories


class Category(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
        blank=True,
        null=True
    )

    objects = CategoryManager()

    def copy(self):
        cloned_obj = self
        cloned_obj.pk = None
        cloned_obj._state.adding = True
        cloned_obj.save()
        return cloned_obj

    def __str__(self) -> str:
        return self.name
# Create your models here.
