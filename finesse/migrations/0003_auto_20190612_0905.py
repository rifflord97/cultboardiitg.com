# Generated by Django 2.2b1 on 2019-06-12 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finesse', '0002_auto_20190612_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club_member',
            old_name='image1',
            new_name='image',
        ),
    ]
