# Generated by Django 4.1.7 on 2023-03-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0003_rename_languaje_language_alter_language_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
