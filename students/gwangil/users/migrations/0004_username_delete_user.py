# Generated by Django 4.0.2 on 2022-02-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'usernames',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]