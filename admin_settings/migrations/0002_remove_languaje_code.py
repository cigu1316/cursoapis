# Generated by Django 4.1.7 on 2023-03-08 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languaje',
            name='code',
        ),
    ]
