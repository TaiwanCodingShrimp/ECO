# Generated by Django 5.0.6 on 2024-05-28 05:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Board", "0007_alter_board_fb_id_alter_board_leftover_item_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="board",
            name="fb_id",
        ),
        migrations.RemoveField(
            model_name="board",
            name="leftover_item",
        ),
        migrations.RemoveField(
            model_name="board",
            name="waste_item",
        ),
        migrations.RemoveField(
            model_name="board",
            name="wo_id",
        ),
    ]
