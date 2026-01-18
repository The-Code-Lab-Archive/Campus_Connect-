from django.contrib import admin
from .models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'members', 'email']
    list_filter = ['category']
    search_fields = ['name', 'description']
