# Generated by Django 2.2.6 on 2019-10-24 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0002_auto_20191024_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='solo',
            new_name='climate',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='weather',
            new_name='terrain',
        ),
    ]
