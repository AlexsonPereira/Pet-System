# Generated by Django 4.1.6 on 2023-02-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0004_alter_trait_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]