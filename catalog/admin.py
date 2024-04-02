from django.contrib import admin

from catalog.models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    ordering = ('id',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image', 'owner', 'is_published',)
    list_display_links = ('id', 'name')
    ordering = ('id',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)



