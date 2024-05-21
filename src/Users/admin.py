# Register your models here.
from django.contrib import admin

from Users.models.datas import Leftover, Waste
from Users.models.user_info import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["users_id", "title", "email"]


class WasteAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "provider", "sent_to"]


class LeftoverAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "provider", "sent_to"]


admin.site.register(User, UserAdmin)
admin.site.register(Waste, WasteAdmin)
admin.site.register(Leftover, LeftoverAdmin)
