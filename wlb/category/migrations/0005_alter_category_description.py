# Generated by Django 4.1.7 on 2024-05-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_add_default_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
