# Generated by Django 3.1.4 on 2021-04-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0039_delete_sitename'),
    ]

    operations = [
        migrations.CreateModel(
            name='siteDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('subName', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]
