from django.db import models

from staff.models import Staff

NULLABLE = {'blank': True, 'null': True}

class Record(models.Model):
    last_name = models.CharField(max_length=20, verbose_name='Фамилия', **NULLABLE)
    name = models.CharField(max_length=20, verbose_name="Имя", **NULLABLE)
    surname = models.CharField(max_length=20, verbose_name='Отчество', **NULLABLE)
    age = models.IntegerField(verbose_name="возраст", **NULLABLE)
    gender = models.CharField(max_length=10, verbose_name="пол", **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    date_recorded = models.DateField(verbose_name="дата записи", **NULLABLE)
    time_recorded = models.TimeField(verbose_name="время записи", **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,
                                 max_length=20, verbose_name='врач', **NULLABLE)
    publication = models.BooleanField(default=True, verbose_name="признак публикации")


    def __str__(self):
        return f'{self.name} {self.surname} {self.age} {self.gender}'

    class Meta:
        verbose_name = 'запись на диагностику'
        verbose_name_plural = 'записи на диагностику'
