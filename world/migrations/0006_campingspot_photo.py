# Generated by Django 3.1.4 on 2021-03-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_remove_campingspot_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='campingspot',
            name='photo',
            field=models.ImageField(default='nopic', upload_to='media'),
            preserve_default=False,
        ),
    ]
