# Generated by Django 3.1.4 on 2021-03-27 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_campingspot_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campingspot',
            name='photo',
        ),
    ]
