from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from enumfields import EnumField

from Organization.models import Food_Bank, WelfareOrganization

from ..schema import CarbonFootprintReportData, CommuteMethod
from .user_info import User


class FootPrint(models.Model):
    distance = models.FloatField(
        default=0.0,
        help_text="移動距離(km)",
        validators=(MinValueValidator(0), MaxValueValidator(100000)),
    )
    method = EnumField(
        CommuteMethod,
        default=CommuteMethod.Car,
        max_length=20,
        help_text="通勤交通方式",
    )
    date = models.DateTimeField("活動時間")
    carbon_footprint = models.FloatField(
        default=0.0,
        verbose_name="累計碳足跡",
        validators=(MinValueValidator(0), MaxValueValidator(100000)),
    )
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def update_carbon_footprint(self):
        self.carbon_footprint = self.get_carbon_footprint()

    def get_carbon_footprint(self):
        return self._get_carbon_footprint() or 0

    def _get_carbon_footprint(self):
        commute_distance = {"commute_distance": self.distance}
        commute_footprint_data = CarbonFootprintReportData(**commute_distance)
        carbon_footprints = commute_footprint_data.commute_carbon_footprints()
        return getattr(carbon_footprints, self.method.value)

    def save(self, *args, **kwargs):
        self.update_carbon_footprint()
        super().save(*args, **kwargs)


class Waste(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=20, null=False)
    sent_to = models.ForeignKey(
        WelfareOrganization, on_delete=models.CASCADE, null=True
    )
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.id)


class FoodTable(models.Model):
    item = models.CharField(max_length=20, primary_key=True)
    carbon_factor = models.FloatField(
        default=0.0,
        help_text="對應碳足跡",
        validators=[MinValueValidator(0), MaxValueValidator(10000)],
    )

    def __str__(self) -> str:
        return str(self.item)


class Leftover(models.Model):
    id = models.AutoField(primary_key=True)
    item: FoodTable = models.ForeignKey(FoodTable, on_delete=models.CASCADE, null=True)
    # item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField()
    label = models.CharField(max_length=20, null=False)
    portion = models.FloatField(
        default=0.0,
        help_text="食物重量",
        validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)],
    )
    sent_to = models.ForeignKey(Food_Bank, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20)

    food_carbon_footprint = models.FloatField(
        default=0.0,
        verbose_name="食物累計碳足跡",
        validators=[MinValueValidator(0), MaxValueValidator(10000)],
    )

    def update_food_footprint(self):
        self.food_carbon_footprint = self.get_foodtable_footprint()

    def get_foodtable_footprint(self):
        return self._get_foodtable_footprint() or 0

    def _get_foodtable_footprint(self):
        if self.item and self.portion:
            return self.item.carbon_factor * self.portion
        return 0

    def save(self, *args, **kwargs):
        self.update_food_footprint()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.id)
