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

class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(max_length=15, verbose_name="телефон")
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    description = models.TextField(null=False, verbose_name="краткое описание")
    name_category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='наименование категории')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано на сайте')


    def __str__(self):
        return f'{self.name} {self.surname} {self.description}'

    class Meta:
        verbose_name = 'персонал'
        verbose_name_plural = 'персонал'
