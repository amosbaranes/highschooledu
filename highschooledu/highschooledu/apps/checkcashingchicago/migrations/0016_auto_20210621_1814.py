# Generated by Django 3.1.11 on 2021-06-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0015_checkcashingweb_footer_main_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_info',
        ),
        migrations.AddField(
            model_name='location',
            name='address1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='address2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='address3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='address4',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
