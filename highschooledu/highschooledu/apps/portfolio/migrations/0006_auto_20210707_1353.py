# Generated by Django 2.1.10 on 2021-07-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210707_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioweb',
            old_name='portfolio_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='portfolioweb',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioweb',
            name='prefix_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]