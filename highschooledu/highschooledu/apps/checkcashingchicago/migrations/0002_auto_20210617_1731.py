# Generated by Django 3.1.11 on 2021-06-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkcashingweb',
            name='main_sub_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='checkcashingweb',
            name='main_sub_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkcashingweb',
            name='main_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
