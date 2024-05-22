from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from enumfields import EnumField

from ..schema import CommuteMethod
from .user_info import User


class FootPrint(models.Model):
    distance: float = models.FloatField(
        default=0.0,
        help_text="移動距離(km)",
        validators=(MinValueValidator(0), MaxValueValidator(100000)),
    )
    method: CommuteMethod = EnumField(
        CommuteMethod,
        default=CommuteMethod.Mrt,
        max_length=10,
        help_text="通勤交通方式",
    )
    date = models.DateTimeField(
        "活動時間",
        auto_now_add=True,
    )
    carbon_footprint = models.FloatField(
        default=0.0,
        verbose_name="累計碳足跡",
        validators=(MinValueValidator(0), MaxValueValidator(100000)),
    )
    user_id: int = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Waste(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField(auto_now_add=True)
    label = models.DateTimeField(max_length=20, null=False)
    sent_to = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.id)


class Leftover(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField(auto_now_add=True)
    label = models.DateTimeField(max_length=20, null=False)
    portion = models.CharField(
        max_length=20,
        null=False,
        validators=(MinValueValidator(0), MaxValueValidator(1000)),
    )
    sent_to = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.id)
