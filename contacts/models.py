from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    email = models.CharField(max_length=100, verbose_name='Ел.почта')
    subject = models.CharField(max_length=100, verbose_name='Субьект')
    message = models.TextField(blank=True, verbose_name='Сповіщення')
    contact_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата')

    class Meta:
        verbose_name_plural = 'Контакт'
        verbose_name = 'Контакт'

    def __str__(self):
        return self.email

