# Generated by Django 5.0.6 on 2024-06-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0015_alter_footprint_date_alter_leftover_date_put_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leftover",
            name="date_put_in",
            field=models.DateField(verbose_name="time"),
        ),
        migrations.AlterField(
            model_name="waste",
            name="date_put_in",
            field=models.DateField(verbose_name="time"),
        ),
    ]
