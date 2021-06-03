# Generated by Django 3.1.11 on 2021-06-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20210602_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['order'], 'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='person/'),
        ),
    ]