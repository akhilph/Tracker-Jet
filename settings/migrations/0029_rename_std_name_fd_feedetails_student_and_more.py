# Generated by Django 4.2.2 on 2023-06-16 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0028_rename_std_name_payment_std_name_p_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedetails',
            old_name='std_name_FD',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='feesreceipt',
            old_name='std_name_FR',
            new_name='student',
        ),
    ]
