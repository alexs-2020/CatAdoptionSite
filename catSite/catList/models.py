from django.db import models
from image_cropping import ImageRatioField


class Cat(models.Model):
    SEX_CHOICES = [
        ('macho', 'Macho'),  # Male
        ('hembra', 'Hembra'),  # Female
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sexo = models.CharField(max_length=6, choices=SEX_CHOICES, default='macho')  # Gender Field
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cats/')
    cropping = ImageRatioField('image', '400x500')  # Set the crop aspect ratio here
    personality_traits = models.CharField(max_length=100)

    def __str__(self):
        return self.name
