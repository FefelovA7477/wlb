from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Metric(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                related_name='metric')
    clicked_get_started_first_screen = models.BooleanField(default=False, 
                                                           verbose_name="Нажал 'поехали' на первом экране")
    clicked_view_example_second_screen = models.BooleanField(default=False, 
                                                             verbose_name="Нажал 'смотреть пример' на втором экране")
    clicked_next_second_screen = models.BooleanField(default=False, 
                                                     verbose_name="Нажал 'далее' на втором экране")
    clicked_add_own_category_third_screen = models.BooleanField(default=False, 
                                                                verbose_name="Нажал 'добавить свою категорию' на третьем экране")
    clicked_next_with_categories_third_screen = models.BooleanField(default=False, 
                                                                    verbose_name="Нажал 'далее' на третьем экране с категориями")
    clicked_time_selection_onboarding = models.BooleanField(default=False, 
                                                            verbose_name="Нажал на выбор времени в онбординге")

    class Meta:
        verbose_name = "Статистика онбординга"
        verbose_name_plural = "Статистики онбордингов"

    def is_completed_all_assessments(self):
        return self.clicked_get_started_first_screen \
                and self.clicked_view_example_second_screen \
                and self.clicked_next_second_screen \
                and self.clicked_add_own_category_third_screen \
                and self.clicked_next_with_categories_third_screen \
                and self.clicked_time_selection_onboarding
# Create your models here.
