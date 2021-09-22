# Generated by Django 3.2.5 on 2021-09-22 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0004_auto_20210920_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='client_amount',
        ),
        migrations.RemoveField(
            model_name='report',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='report',
            name='service_amount',
        ),
        migrations.RemoveField(
            model_name='report',
            name='services',
        ),
        migrations.AddField(
            model_name='report',
            name='json_client',
            field=models.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='report',
            name='json_service',
            field=models.JSONField(default=''),
        ),
    ]