# Generated by Django 4.2.2 on 2024-04-03 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rank',
            options={'verbose_name': 'специализация', 'verbose_name_plural': 'специализации'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='name_category',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='staff.rank', verbose_name='наименование специализации'),
        ),
    ]
