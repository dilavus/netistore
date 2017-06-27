from django.contrib import admin
from main.models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Items, ItemAdmin)
admin.site.register(Category, CategoryAdmin)

