# Generated by Django 5.0.6 on 2024-05-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Board", "0003_alter_board_fb_id_alter_board_leftover_item_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="user_id",
            field=models.CharField(max_length=20, verbose_name="使用者編號"),
        ),
    ]
