# Generated by Django 2.1.5 on 2019-03-06 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190305_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 5, 1, 34, 661600), verbose_name='date published'),
        ),
    ]