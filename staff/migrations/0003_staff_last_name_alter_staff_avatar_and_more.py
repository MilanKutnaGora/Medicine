# Generated by Django 4.2.2 on 2024-04-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_rank_options_alter_staff_name_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(verbose_name='заслуги и регалии'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='рабочий телефон'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
    ]