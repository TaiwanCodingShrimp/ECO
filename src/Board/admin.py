
from django.contrib import admin

from .forms import BoardForm
from .models import Board


class BoardAdmin(admin.ModelAdmin):
    form = BoardForm  # 指定使用自定義表單
    list_display = [
        "board_id",
        "user",
        "topic",
        "date",

        "leftover_item",
        "waste_item",
        "fb_id",
        "wo_id",
    ]

    fields = (
        "topic",
        "content",
        "type",
        "leftover_item",
        "waste_item",
        "fb_id",
        "wo_id",
    )
    readonly_fields = ("date",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



admin.site.register(Board, BoardAdmin)
