# Generated by Django 4.1.7 on 2023-03-27 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0008_alter_card_valid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='valid_date',
            field=models.DateField(default='mm/yy', max_length=5),
        ),
    ]
