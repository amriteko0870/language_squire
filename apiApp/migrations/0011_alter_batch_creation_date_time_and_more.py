# Generated by Django 4.0.3 on 2023-03-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0010_batch_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch_creation',
            name='date_time',
            field=models.TextField(default='2023-03-05 15:27:49.688302+05:30'),
        ),
        migrations.AlterField(
            model_name='user_login',
            name='batch_id',
            field=models.TextField(default='u'),
        ),
    ]
