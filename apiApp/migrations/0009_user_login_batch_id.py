# Generated by Django 4.0.3 on 2023-03-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0008_alter_test_assigned_listening_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_login',
            name='batch_id',
            field=models.TextField(blank=True),
        ),
    ]
