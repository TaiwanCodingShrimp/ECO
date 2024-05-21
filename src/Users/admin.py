# Register your models here.
from django.contrib import admin

from .models import FootPrint, Leftover, User, Waste


class UserAdmin(admin.ModelAdmin):
    list_display = ["users_id", "title", "email"]


class WasteAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "provider", "sent_to"]


class LeftoverAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "provider", "sent_to"]


class FootPrintAdmin(admin.ModelAdmin):
    list_display = ["distance", "date", "method", "carbon_footprint"]


admin.site.register(User, UserAdmin)
admin.site.register(Waste, WasteAdmin)
admin.site.register(Leftover, LeftoverAdmin)
admin.site.register(FootPrint, FootPrintAdmin)
