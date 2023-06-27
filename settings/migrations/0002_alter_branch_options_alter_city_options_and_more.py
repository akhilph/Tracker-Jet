# Generated by Django 4.2.1 on 2023-05-26 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="branch",
            options={"verbose_name": "branch", "verbose_name_plural": "Branches"},
        ),
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name": "city", "verbose_name_plural": "Cities"},
        ),
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "course", "verbose_name_plural": "Courses"},
        ),
        migrations.AlterModelOptions(
            name="district",
            options={"verbose_name": "district", "verbose_name_plural": "Districts"},
        ),
        migrations.AlterModelOptions(
            name="state",
            options={"verbose_name": "state", "verbose_name_plural": "States"},
        ),
    ]
