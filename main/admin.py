from django.contrib import admin
from main.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent')
    list_filter = ('menu_name',)
    search_fields = ('name', 'url', 'named_url')


admin.site.register(MenuItem, MenuItemAdmin)
