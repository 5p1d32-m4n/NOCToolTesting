# Generated by Django 3.2.4 on 2021-06-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(choices=[('Tecnico', 'Tecnico'), ('Servicio al Cliente', 'Servicio al Cliente')], default='Tecnico', max_length=50),
            preserve_default=False,
        ),
    ]