# Generated by Django 4.0.3 on 2023-02-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0007_test_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_assigned',
            name='listening_score',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test_assigned',
            name='reading_score',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test_assigned',
            name='speaking_remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test_assigned',
            name='speaking_score',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test_assigned',
            name='writing_remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='test_assigned',
            name='writing_score',
            field=models.TextField(blank=True),
        ),
    ]
