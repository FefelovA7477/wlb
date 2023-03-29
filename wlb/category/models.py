from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DEFAULT_CATEGORY_LIST = (
    'Спорт', 
    'Питание', 
    'Сон',
    'Отдых',
)

class CategoryCustomManager(models.Manager):
    def add_default_categories(self, user: User) -> None:
        for name in DEFAULT_CATEGORY_LIST:
            user.categories.add(self.create(
                name=name,
                user=user
            ))
            # user.save()



class Category(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    objects = CategoryCustomManager()

    def __str__(self) -> str:
        return self.name
# Create your models here.
