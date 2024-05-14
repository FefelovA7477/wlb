from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('tg_chat_id', 'is_new')


admin.site.register(User, UserAdmin)
# Register your models here.
