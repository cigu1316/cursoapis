# Generated by Django 4.1.7 on 2023-03-28 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coins', '0019_alter_card_color_alter_card_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('purple', 'purple'), ('blue', 'blue'), ('green', 'green'), ('orange', 'orange')], default='purple', max_length=7),
        ),
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='card',
            name='valid_date',
            field=models.DateTimeField(default='mm/yy', max_length=5),
        ),
    ]
