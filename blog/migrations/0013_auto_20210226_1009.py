# Generated by Django 3.1.6 on 2021-02-26 10:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210226_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 10, 9, 39, 196621, tzinfo=utc)),
        ),
    ]
