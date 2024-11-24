from django.contrib import admin
from .models import Cat
from image_cropping import ImageCroppingMixin

@admin.register(Cat)
class CatAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'age', 'breed')