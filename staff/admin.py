from django.contrib import admin

from staff.models import Rank, Staff


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    ordering = ('id',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone', 'email', 'avatar', 'description', 'name_category', 'is_published')
    list_display_links = ('id', 'name')
    ordering = ('id',)
    list_filter = ('category',)
    search_fields = ('surname', 'description',)
