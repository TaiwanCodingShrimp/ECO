# Create your models here.
from django.db import models
from enumfields import EnumField

from .schema import OrganizationType


class WelfareOrganization(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=20)
    county: str = models.CharField(max_length=20)
    district: str = models.CharField(max_length=20)
    type: OrganizationType = EnumField(
        OrganizationType,
        default=OrganizationType.Government,
        max_length=10,
        help_text="所屬類型",
    )
    phone: str = models.CharField(max_length=10)
    address: str = models.CharField(max_length=60, null=True)

    def __str__(self) -> str:
        return str(self.name)


class Food_Bank(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=20)
    county: str = models.CharField(max_length=20)
    district: str = models.CharField(max_length=20, default=" ")
    address: str = models.CharField(max_length=20)
    contact: str = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.name)
