# Generated by Django 3.1.4 on 2021-04-11 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0030_auto_20210411_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 16, 11, 49, 999786, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trending',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 16, 11, 50, 1782, tzinfo=utc)),
        ),
    ]
