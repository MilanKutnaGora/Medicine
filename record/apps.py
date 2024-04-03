from django.apps import AppConfig


class RecordConfig(AppConfig):
    verbose_name = "Запись к врачу"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'record'
