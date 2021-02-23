# Generated by Django 3.1.6 on 2021-02-23 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 10, 53, 13, 417189, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 10, 53, 13, 417216), max_length=200, unique=True),
        ),
    ]
