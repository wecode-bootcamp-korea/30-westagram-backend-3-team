# Generated by Django 4.0.2 on 2022-02-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=40, null=True, unique=True),
        ),
    ]
