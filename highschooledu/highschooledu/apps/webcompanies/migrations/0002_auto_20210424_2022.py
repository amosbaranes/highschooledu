# Generated by Django 3.0.10 on 2021-04-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('webcompanies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcompanies',
            name='target_ct',
            field=models.ForeignKey(blank=True, limit_choices_to={'model__in': ('fabhoseafricaweb', 'bizland')}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='webcompanies', to='contenttypes.ContentType'),
        ),
    ]