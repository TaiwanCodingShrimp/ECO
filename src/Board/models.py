from django.db import models
from enumfields import EnumField

from Organization.models import Food_Bank, WelfareOrganization
from Users.models.datas import Leftover, Waste
from Users.models.user_info import User

from .schema import BoardType


class Board(models.Model):
    board_id: int = models.AutoField(primary_key=True, verbose_name="看板編號")
    user_id: User = models.ForeignKey(
        User, verbose_name=("使用者編號"), on_delete=models.CASCADE
    )
    topic: str = models.CharField(max_length=100, verbose_name="標題")
    content: str = models.CharField(max_length=100000, verbose_name="內容", null=True)
    date = models.DateField(auto_now_add=True)
    type: BoardType = EnumField(
        BoardType,
        default=BoardType.Government,
        max_length=10,
    )
    leftover_item: Leftover = models.ForeignKey(
        Leftover,
        verbose_name=("剩食編號"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    waste_item: Waste = models.ForeignKey(
        Waste,
        verbose_name=("二手物品編號"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    fb_id: Food_Bank = models.ForeignKey(
        Food_Bank,
        verbose_name=("食物銀行"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    wo_id: WelfareOrganization = models.ForeignKey(
        WelfareOrganization,
        verbose_name=("社福機構"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.board_id)
