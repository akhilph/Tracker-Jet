# Generated by Django 4.2.1 on 2023-06-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0024_batch_status"),
    ]

    operations = [
        migrations.RemoveField(model_name="batch", name="status",),
    ]