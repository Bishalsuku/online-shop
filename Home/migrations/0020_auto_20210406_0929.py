# Generated by Django 3.1.6 on 2021-04-06 03:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_auto_20210406_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 3, 44, 2, 402684, tzinfo=utc)),
        ),
    ]
