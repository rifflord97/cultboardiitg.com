# Generated by Django 2.2b1 on 2019-06-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpressions', '0005_auto_20190611_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_member',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='./xpressions/members'),
        ),
        migrations.AlterField(
            model_name='club_member',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='./xpressions/members'),
        ),
        migrations.AlterField(
            model_name='club_member',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='./xpressions/members'),
        ),
        migrations.AlterField(
            model_name='club_sec',
            name='image',
            field=models.FileField(upload_to='./xpressions/'),
        ),
    ]
