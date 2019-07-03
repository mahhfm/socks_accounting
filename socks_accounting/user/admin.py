from django.contrib import admin
from . import models
from django.contrib.auth.models import User, Permission


admin.site.register(models.Profile)
admin.site.register(models.Service)
admin.site.register(models.Order)
