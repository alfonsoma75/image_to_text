from django.contrib import admin

from .models import ImageModel


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    model = ImageModel
