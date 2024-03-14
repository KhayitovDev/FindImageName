from django.contrib import admin
from .models import ImageGame, Languages

# Register your models here.

@admin.register(ImageGame)
class ImageGameAdmin(admin.ModelAdmin):
    list_display=['language_preference', 'created_at']

admin.site.register(Languages)