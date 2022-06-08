# Generated by Django 3.1.4 on 2021-04-11 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0027_auto_20210409_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='siteName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('SubTitle', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 15, 44, 39, 581774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trending',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 15, 44, 39, 584777, tzinfo=utc)),
        ),
    ]
