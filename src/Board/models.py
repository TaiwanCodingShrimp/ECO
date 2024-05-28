from django.db import models
from enumfields import EnumField

from Organization.models import Food_Bank, WelfareOrganization
from Users.models.datas import Leftover, Waste
from Users.models.user_info import User

from .schema import BoardType


class Board(models.Model):
    board_id = models.AutoField(
        primary_key=True,
        verbose_name="看板編號",
    )
    user = models.ForeignKey(
        User,
        verbose_name="使用者編號",
        on_delete=models.CASCADE,
        null=True,
    )
    topic = models.CharField(
        max_length=100,
        verbose_name="標題",
    )
    content = models.CharField(
        max_length=100000,
        verbose_name="內容",
        null=True,
    )
    date = models.DateField(
        auto_now_add=True,
    )
    type = EnumField(
        BoardType,
        default=BoardType.Government,
        max_length=10,
    )
    leftover_item = models.ForeignKey(
        Leftover,
        verbose_name="剩食編號",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    waste_item = models.ForeignKey(
        Waste,
        verbose_name="二手物品編號",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    fb_id = models.ForeignKey(
        Food_Bank,
        verbose_name="食物銀行",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    wo_id = models.ForeignKey(
        WelfareOrganization,
        verbose_name="社福機構",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    def __str__(self):
        return str(self.board_id)
