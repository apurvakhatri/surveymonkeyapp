# Generated by Django 2.0.5 on 2018-05-07 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20180507_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yellowusertoken',
            name='user',
        ),
    ]
