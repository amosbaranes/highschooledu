# Generated by Django 3.1.11 on 2021-06-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0014_auto_20210621_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkcashingweb',
            name='footer_main_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
