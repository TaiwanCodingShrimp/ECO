# Generated by Django 5.0.6 on 2024-05-26 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Board", "0002_alter_board_fb_id_alter_board_leftover_item_and_more"),
        ("Organization", "0002_welfareorganization_delete_welfare_organization"),
        ("Users", "0005_footprint_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="fb_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Organization.food_bank",
                verbose_name="食物銀行",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="leftover_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Users.leftover",
                verbose_name="剩食編號",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="waste_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Users.waste",
                verbose_name="二手物品編號",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="wo_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Organization.welfareorganization",
                verbose_name="社福機構",
            ),
        ),
    ]
