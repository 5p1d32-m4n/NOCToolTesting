# Generated by Django 3.2.5 on 2021-09-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0002_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='client_amount',
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_amount',
        ),
        migrations.AddField(
            model_name='report',
            name='client_amount',
            field=models.CharField(blank=True, default='0', max_length=250),
        ),
        migrations.AddField(
            model_name='report',
            name='service_amount',
            field=models.CharField(blank=True, default='0', max_length=250),
        ),
        migrations.RemoveField(
            model_name='report',
            name='causes',
        ),
        migrations.AddField(
            model_name='report',
            name='causes',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
        migrations.RemoveField(
            model_name='report',
            name='clients',
        ),
        migrations.AddField(
            model_name='report',
            name='clients',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
        migrations.RemoveField(
            model_name='report',
            name='outage_type',
        ),
        migrations.AddField(
            model_name='report',
            name='outage_type',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
        migrations.RemoveField(
            model_name='report',
            name='services',
        ),
        migrations.AddField(
            model_name='report',
            name='services',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
    ]
