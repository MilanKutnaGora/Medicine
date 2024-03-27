from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100, verbose_name="заголовок")
    description = models.TextField(null=False, verbose_name="содержимое")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    publication = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="колличество просмотров")

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'запись на диагностику'
        verbose_name_plural = 'записи на диагностику'
