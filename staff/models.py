from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Rank(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'специализация'
        verbose_name_plural = "специализации"

class Staff(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Отчество")
    phone = models.CharField(max_length=15, verbose_name="рабочий телефон")
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(verbose_name='аватар', **NULLABLE)
    description = models.TextField(null=False, verbose_name="заслуги и регалии")
    name_category = models.ForeignKey(Rank, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='наименование специализации')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано на сайте')


    def __str__(self):
        return f'{self.last_name} {self.name} {self.surname}'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
