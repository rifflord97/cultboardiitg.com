# Generated by Django 2.2b1 on 2019-06-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpressions', '0002_auto_20190609_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_member',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='club_member',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='club_sec',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='club_sec',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]