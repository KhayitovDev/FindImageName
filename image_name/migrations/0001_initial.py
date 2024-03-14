# Generated by Django 5.0.3 on 2024-03-11 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('input_field', models.CharField(blank=True, max_length=550)),
                ('correct_answer_field', models.CharField(max_length=550)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_name.languages')),
            ],
        ),
    ]