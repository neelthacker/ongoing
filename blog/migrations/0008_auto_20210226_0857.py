# Generated by Django 3.1.6 on 2021-02-26 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210226_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 8, 57, 30, 682680, tzinfo=utc)),
        ),
    ]
