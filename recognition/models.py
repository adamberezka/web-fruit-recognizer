from django.db import models
from django.utils.translation import gettext_lazy as _


class UploadedImage(models.Model):
    class Fruit(models.TextChoices):
        NONE = 'NONE', _('None')
        BANANA = 'BANANA', _('Banana')
        HUCKLEBERRY = 'HUCKLEBERRY', _('Huckleberry')
        KIWI = 'KIWI', _('Kiwi')
        LEMON = 'LEMON', _('Lemon')
        MANGO = 'MANGO', _('Mango')
        PINEAPPLE = 'PINEAPPLE', _('Pineapple')
        PLUM = 'PLUM', _('Plum')
        RASPBERRY = 'RASPBERRY', _('Raspberry')
        STRAWBERRY = 'STRAWBERRY', _('Strawberry')
        WATERMELON = 'WATERMELON', _('Watermelon')

    image = models.ImageField(upload_to='images')
    fruit = models.CharField(
        max_length=32,
        choices=Fruit.choices,
        default=Fruit.NONE
    )
    prediction = models.CharField(
        max_length=32,
        choices=Fruit.choices,
        default=Fruit.NONE
    )
