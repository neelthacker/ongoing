# Generated by Django 3.0.3 on 2021-04-30 05:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210430_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 5, 12, 59, 235533, tzinfo=utc)),
        ),
    ]
