# Generated by Django 3.0.3 on 2021-05-05 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='text',
            new_name='value',
        ),
    ]
