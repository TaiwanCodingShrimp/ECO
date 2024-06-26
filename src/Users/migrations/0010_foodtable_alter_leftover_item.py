# Generated by Django 5.0.6 on 2024-06-11 12:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0009_alter_leftover_label_alter_leftover_portion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodTable",
            fields=[
                (
                    "item",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "carbon_factor",
                    models.FloatField(
                        default=0.0,
                        help_text="對應碳足跡",
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10000),
                        ],
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="leftover",
            name="item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Users.foodtable",
            ),
        ),
    ]
