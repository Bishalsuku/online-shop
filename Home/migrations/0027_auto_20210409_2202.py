# Generated by Django 3.1.2 on 2021-04-09 16:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0026_auto_20210409_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 16, 17, 5, 684649, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added', models.DateTimeField(default=datetime.datetime(2021, 4, 9, 16, 17, 5, 684649, tzinfo=utc))),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]