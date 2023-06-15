from django.contrib import admin
from .models import TreeMenu, TreeMenuCategories
"""
Register the created models 
for their processing by the administrator
"""

@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'link', 'parent',)
    list_display_links = ('pk', 'name',)


@admin.register(TreeMenuCategories)
class TreeMenuCategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'systemic_name',)
    list_display_links = ('pk', 'name',)
    
