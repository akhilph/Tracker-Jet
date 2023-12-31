# Generated by Django 4.2.2 on 2023-06-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0030_studentfees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_fees',
            name='fees_type',
            field=models.CharField(choices=[('Registration', 'Registration'), ('one_times', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='BalanceAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='InstallmentAmount',
            field=models.IntegerField(null=True),
        ),
    ]
