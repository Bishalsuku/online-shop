# Generated by Django 3.1.6 on 2021-04-06 03:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_auto_20210130_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 3, 38, 42, 124405, tzinfo=utc)),
        ),
    ]
