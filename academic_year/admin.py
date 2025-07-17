from django.contrib import admin
from .models import Academic_year

# Register your models here.

class Academic_yearAdmin(admin.ModelAdmin):
    list_display = ['year_name', 'start_date', 'end_date', 'updated_at']
    search_fields = ['status', 'year_name']

admin.site.register(Academic_year, Academic_yearAdmin)
