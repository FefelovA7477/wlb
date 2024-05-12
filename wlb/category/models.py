from django.db import models
from django.contrib.auth import get_user_model
from typing import List

User = get_user_model()

COLOR_CHOICES = (
    ('#45714e', 'green'),
    ('#5e7e66', 'dark-green'),
    ('#d76e16', 'orange'),
    ('#0a093f', 'dark-blue'),
    ('#63a1af', 'biruzoviy'),
    ('#9b2226', 'red'),
    ('#9c52f5', 'violet'),
    ('#fdb917', 'yellow'),
    ('#552222', 'govno-color'),
)


class CategoryManager(models.Manager):
    def clone_default_categories(self) -> List[object | None]:
        default_categories = self.get_queryset().filter(is_default=True)
        cloned_default_categories = [category.copy() for category in default_categories]
        return cloned_default_categories


class Category(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField(default=1)
    description = models.TextField(default='', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    color = models.CharField(max_length=7, 
                             choices=COLOR_CHOICES, 
                             blank=True, 
                             null=True, 
                             default=None)
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
        if cloned_obj.is_default:
            cloned_obj.is_default = False
        cloned_obj.save()
        return cloned_obj

    def __str__(self) -> str:
        return self.name
# Create your models here.
