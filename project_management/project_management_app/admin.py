from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import CustomUser, Project, Sprint

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Sprint)
