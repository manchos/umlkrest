from django.contrib import admin

# Register your models here.

from api.models import Object
from django.contrib import admin


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'created_at', 'modified_at')