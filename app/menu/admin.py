from django.contrib import admin

from .models import TreeMenu


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'depth')
    search_fields = ['name', 'depth']
    list_filter = ['depth']
    raw_id_fields = ('parent',)