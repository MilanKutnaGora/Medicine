# Generated by Django 4.2.2 on 2024-04-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, default='82036215', max_length=8, null=True, verbose_name='код подтверждения почты'),
        ),
    ]
