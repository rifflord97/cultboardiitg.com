# Generated by Django 2.2b1 on 2019-05-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190524_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcoming_events',
            name='image',
            field=models.FileField(upload_to='Upcoming_Events'),
        ),
    ]
