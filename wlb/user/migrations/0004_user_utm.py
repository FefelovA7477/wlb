# Generated by Django 4.1.7 on 2024-05-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_tg_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='utm',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
