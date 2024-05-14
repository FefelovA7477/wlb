# Generated by Django 4.1.7 on 2024-05-12 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20240511_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, choices=[('#45714e', 'green'), ('#5e7e66', 'dark-green'), ('#d76e16', 'orange'), ('#0a093f', 'dark-blue'), ('#63a1af', 'biruzoviy'), ('#9b2226', 'red'), ('#9c52f5', 'violet'), ('#fdb917', 'yellow'), ('#552222', 'govno-color'), ('#32CD32', 'light-green')], default=None, max_length=7, null=True),
        ),
    ]
