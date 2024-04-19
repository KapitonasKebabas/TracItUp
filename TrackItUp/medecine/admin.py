from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.UserMedecine)
admin.site.register(models.AprovedMedecine)
admin.site.register(models.OrderStatus)
admin.site.register(models.Orders)