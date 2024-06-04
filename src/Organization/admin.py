# Register your models here.
from django.contrib import admin

from .models import Food_Bank, WelfareOrganization


class WoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "district", "address", "type", "phone"]


class FbAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "contact"]


admin.site.register(WelfareOrganization, WoAdmin)
admin.site.register(Food_Bank, FbAdmin)
