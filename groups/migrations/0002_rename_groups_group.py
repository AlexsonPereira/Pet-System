# Generated by Django 4.1.6 on 2023-02-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
    ]
