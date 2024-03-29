# Generated by Django 4.0.3 on 2023-03-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0014_batch_creation_assignment_array_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_assigned',
            name='listening_answers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='test_assigned',
            name='reading_answers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='test_assigned',
            name='speaking_answers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='test_assigned',
            name='writing_answers',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='batch_creation',
            name='date_time',
            field=models.TextField(default='2023-03-12 19:27:31.237305+05:30'),
        ),
        migrations.AlterField(
            model_name='user_login',
            name='date_time',
            field=models.TextField(default='2023-03-12 19:27:31.237305+05:30'),
        ),
    ]
