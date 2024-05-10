from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from category.models import Category
from django.utils import timezone

User = get_user_model()

def get_today():
    return timezone.now().date()

class Score(models.Model):
    score = models.FloatField(
        default=0, 
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='scores'
    )
    date = models.DateField(default=get_today)

    class Meta:
        unique_together = ('category', 'date')
    
# Create your models here.
