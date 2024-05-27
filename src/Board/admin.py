# Register your models here.

from django.contrib import admin

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = [
        "board_id",
        "user_id",
        "leftover_item",
        "waste_item",
        "fb_id",
        "wo_id",
    ]


admin.site.register(Board, BoardAdmin)
