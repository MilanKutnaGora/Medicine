from django.contrib import admin

from staff.models import Rank, Staff


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'name', 'surname', 'phone', 'email', 'avatar', 'description', 'name_category', 'is_published')
    list_display_links = ('id', 'last_name')
    ordering = ('id',)
    search_fields = ('last_name', 'description',)
