# Generated by Django 4.1.6 on 2023-02-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0002_trait_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
