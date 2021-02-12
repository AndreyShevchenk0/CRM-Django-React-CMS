from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Опис')
    phone = models.CharField(max_length=20, verbose_name='номер телефону')
    email = models.CharField(max_length=100, verbose_name='Ел.адреса ')
    top_seller = models.BooleanField(default=False, verbose_name='Топ продавець')
    date_hired = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата створення')

    class Meta:
        verbose_name_plural = 'Створити Риелтора'
        verbose_name = 'Створити Риелтора'

    def __str__(self):
        return self.name
