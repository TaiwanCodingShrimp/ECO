from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [
            "topic",
            "content",
            "type",
            "leftover_item",
            "waste_item",
            "fb_id",
            "wo_id",
        ]
