# Generated by Django 3.1.11 on 2021-06-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0006_auto_20210619_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='location',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='location',
            name='title',
        ),
        migrations.AddField(
            model_name='checkcashingweb',
            name='background_currency_image',
            field=models.ImageField(blank=True, null=True, upload_to='currency/'),
        ),
        migrations.AddField(
            model_name='checkcashingweb',
            name='background_location_image',
            field=models.ImageField(blank=True, null=True, upload_to='location/'),
        ),
        migrations.AddField(
            model_name='checkcashingweb',
            name='location_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
