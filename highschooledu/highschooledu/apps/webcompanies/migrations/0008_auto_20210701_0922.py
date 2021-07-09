# Generated by Django 2.1.10 on 2021-07-01 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webcompanies', '0007_auto_20210617_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcompanies',
            name='target_ct',
            field=models.ForeignKey(blank=True, limit_choices_to={'model__in': ('fabhoseafricaweb', 'bizlandweb', 'radiusfoodweb', 'countries', 'institutionweb', 'checkcashingweb', 'portfolioweb')}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webcompanies', to='contenttypes.ContentType'),
        ),
    ]
