# Create your models here.
from django.db import models
from enumfields import EnumField

from .schema import Organization_type


class Welfare_Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    type: Organization_type = EnumField(
        Organization_type,
        default=Organization_type.Government,
        max_length=10,
        help_text="所屬類型",
    )
    phone = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.id)


class Food_Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.id)
