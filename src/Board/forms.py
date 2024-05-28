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
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "標題"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "內容", "rows": 5}
            ),
        }