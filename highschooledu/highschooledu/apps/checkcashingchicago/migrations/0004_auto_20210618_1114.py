# Generated by Django 3.1.11 on 2021-06-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0003_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_info',
            field=models.CharField(max_length=300, null=True),
        ),
    ]