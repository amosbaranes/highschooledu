# Generated by Django 3.1.11 on 2021-06-20 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkcashingchicago', '0010_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='slug',
        ),
    ]
