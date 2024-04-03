# Generated by Django 4.2.2 on 2024-04-03 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_rank_options_alter_staff_name_category'),
        ('record', '0004_record_date_recorded_record_time_recorded'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='staff',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='имя персонала'),
        ),
    ]