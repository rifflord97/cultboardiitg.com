# Generated by Django 2.2b1 on 2019-06-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manthan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='photos',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
