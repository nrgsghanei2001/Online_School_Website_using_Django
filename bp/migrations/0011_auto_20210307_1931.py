# Generated by Django 3.1.7 on 2021-03-07 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0010_auto_20210307_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 7, 19, 31, 15, 31954)),
        ),
        migrations.AlterField(
            model_name='videos',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
