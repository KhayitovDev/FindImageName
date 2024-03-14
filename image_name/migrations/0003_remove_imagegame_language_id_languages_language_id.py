# Generated by Django 5.0.3 on 2024-03-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_name', '0002_imagegame_language_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagegame',
            name='language_id',
        ),
        migrations.AddField(
            model_name='languages',
            name='language_id',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
