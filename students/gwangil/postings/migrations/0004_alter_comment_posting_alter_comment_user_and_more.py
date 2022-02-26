# Generated by Django 4.0.2 on 2022-02-25 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone_number'),
        ('postings', '0003_remove_posting_image_url_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='postings.posting'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.user'),
        ),
        migrations.AlterField(
            model_name='image',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='postings.posting'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postings', to='users.user'),
        ),
    ]
