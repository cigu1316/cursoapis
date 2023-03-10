# Generated by Django 4.1.7 on 2023-03-09 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_settings', '0003_rename_languaje_language_alter_language_options'),
        ('users', '0004_rename_adrress_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='availability',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time'), ('freelance', 'freelance'), ('other', 'other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_settings.country'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='cover_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_settings.language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='years_of_experience',
            field=models.IntegerField(),
        ),
    ]
