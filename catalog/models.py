from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"



class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/',  verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='наименование категории')
    price = models.IntegerField(verbose_name='цена за услугу')
    date_base = models.DateField(null=True, blank=True, verbose_name='дата создания')
    date_change = models.DateField(null=True, blank=True, verbose_name='дата изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.SET_NULL,
                              **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано на сайте')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'медицинская услуга'
        verbose_name_plural = 'медицинские услуги'

        permissions = [
            (
                'set_published_status',
                'can publish service'
            )
        ]



