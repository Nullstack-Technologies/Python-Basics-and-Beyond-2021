from django.contrib import admin

from .models import CovidResource


@admin.register(CovidResource)
class CovidResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'contact_number']
