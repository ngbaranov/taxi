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