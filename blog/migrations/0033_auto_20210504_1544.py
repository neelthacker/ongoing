# Generated by Django 3.0.3 on 2021-05-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20210430_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
