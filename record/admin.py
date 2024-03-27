from django.contrib import admin

from record.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    ordering = ('id',)





