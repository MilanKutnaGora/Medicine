# Generated by Django 4.2.2 on 2024-04-03 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_last_name_alter_staff_avatar_and_more'),
        ('record', '0005_record_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='staff',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='врач'),
        ),
    ]