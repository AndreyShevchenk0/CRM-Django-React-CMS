from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'Продаж'
        FOR_RENT = 'Аренда'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Имя риелтора')
    slug = models.CharField(max_length=200, unique=True, verbose_name='Слаг')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    address = models.CharField(max_length=150, verbose_name='Адреса')
    city = models.CharField(max_length=100, verbose_name='Місто')
    state = models.CharField(max_length=100, verbose_name='Область')
    zipcode = models.CharField(max_length=15, verbose_name='Код')
    description = models.TextField(blank=True, verbose_name='Опис')
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE, verbose_name='Тип')
    price = models.IntegerField(verbose_name='Ціна')
    bedrooms = models.IntegerField(verbose_name='Кімнат')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Санвузол')
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE, verbose_name='Тип')
    sqft = models.IntegerField(verbose_name='Мін ціна')
    open_house = models.BooleanField(default=False, verbose_name='Відкритий')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_19 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_20 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = 'Оголошення'
        verbose_name = 'Оголошення'

    def __str__(self):
        return self.title
