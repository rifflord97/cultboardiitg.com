# Generated by Django 2.2b1 on 2019-05-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_team_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]