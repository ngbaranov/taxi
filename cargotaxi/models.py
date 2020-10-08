from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заглавие')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Домашняя'
        verbose_name_plural = 'Домашнии'

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

class Price(models.Model):
    title = models.CharField(max_length=100, verbose_name='Марка')
    body_volume = models.CharField(max_length=100, verbose_name='Объем кузова')
    cargo = models.CharField(max_length=100, verbose_name='Грузоподъемность')
    body_length = models.CharField(max_length=200, verbose_name='Длина кузова')
    body_width = models.CharField(max_length=200, verbose_name='Ширина кузова')
    title_height = models.CharField(max_length=200, verbose_name='Высота кузова')
    price_taxi = models.CharField(max_length=200, verbose_name='Цена за час')
    photo_taxi = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

        