# Generated by Django 4.1.6 on 2023-02-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_groups_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
