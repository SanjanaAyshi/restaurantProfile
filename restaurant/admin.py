from django.contrib import admin
from .models import Food, Tag

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_special', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_special', 'created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
 #admin@gmail.com
 #Admin@123
