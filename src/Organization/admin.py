# Register your models here.
from django.contrib import admin

from .models import Food_Bank as fb
from .models import Welfare_Organization as wo

__all__ = [admin, wo, fb]


class WoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "phone"]


class FbAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "county", "contact"]


admin.site.register(wo, WoAdmin)
admin.site.register(fb, FbAdmin)
