from django.contrib import admin

from record.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'surname', 'age', 'gender', 'phone', 'date_recorded', 'time_recorded', 'staff')
    ordering = ('id', 'last_name', 'date_recorded', 'time_recorded')





