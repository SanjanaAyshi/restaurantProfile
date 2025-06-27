from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


# Register your models here.
