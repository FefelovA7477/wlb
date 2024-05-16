from django.contrib import admin

from .models import Metric


class MetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_login_time', 'clicked_get_started_first_screen',
                    'clicked_view_example_second_screen', 'clicked_next_second_screen',
                    'clicked_add_own_category_third_screen', 'clicked_next_with_categories_third_screen',
                    'clicked_time_selection_onboarding', 'is_completed_all_assessments')
    
    @admin.display(description='Дата создания')
    def get_user_login_time(self, obj):
        try:
            return obj.user.date_joined
        except:
            return None

    @admin.display(description='Прошел оценку всех параметров')
    def is_completed_all_assessments(self, obj):
        try:
            return obj.is_completed_all_assessments()
        except:
            return False
    is_completed_all_assessments.boolean = True

admin.site.register(Metric, MetricAdmin)

# Register your models here.
