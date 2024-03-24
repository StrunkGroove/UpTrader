from django.contrib import admin

from .models import TreeMenu


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'depth')
    search_fields = ['name']
