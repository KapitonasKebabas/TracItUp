from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the fieldsets or add_fieldsets attribute
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('age',)}),
    )

# Register your models here.
admin.site.register(models.CustomUser, CustomUserAdmin)