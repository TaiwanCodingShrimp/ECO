# Register your models here.
from django.contrib import admin

from .models import Food_Bank, Welfare_Organization


class WoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "phone"]


class FbAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "contact"]


admin.site.register(Welfare_Organization, WoAdmin)
admin.site.register(Food_Bank, FbAdmin)
