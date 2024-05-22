# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

__all__ = [MaxValueValidator, MinValueValidator, models]


class Welfare_Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    county = models.CharField(max_length=20, null=False)
    district = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        return str(self.id)


class Food_Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    county = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    contact = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.id)
