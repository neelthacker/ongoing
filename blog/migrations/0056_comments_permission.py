# Generated by Django 3.0.3 on 2021-05-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_auto_20210512_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='permission',
            field=models.BooleanField(default=False),
        ),
    ]
