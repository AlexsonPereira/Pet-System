# Generated by Django 4.1.6 on 2023-02-10 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='created_at',
        ),
    ]