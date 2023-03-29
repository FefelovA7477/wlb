# Generated by Django 4.1.7 on 2023-03-28 01:40

from django.db import migrations, models
import notification.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=notification.models.set_default_time)),
            ],
        ),
    ]
