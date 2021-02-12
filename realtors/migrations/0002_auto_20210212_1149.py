# Generated by Django 3.0.4 on 2021-02-12 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realtor',
            options={'verbose_name': 'Створити Риелтора', 'verbose_name_plural': 'Створити Риелтора'},
        ),
        migrations.AlterField(
            model_name='realtor',
            name='date_hired',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Ел.адреса '),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='номер телефону'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='top_seller',
            field=models.BooleanField(default=False, verbose_name='Топ продавець'),
        ),
    ]