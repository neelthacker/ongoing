# Generated by Django 3.1.6 on 2021-02-26 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210226_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 8, 29, 31, 704271, tzinfo=utc)),
        ),
    ]
