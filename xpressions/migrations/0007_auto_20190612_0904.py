# Generated by Django 2.2b1 on 2019-06-12 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpressions', '0006_auto_20190611_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(upload_to='./xpressions/gallery'),
        ),
    ]
