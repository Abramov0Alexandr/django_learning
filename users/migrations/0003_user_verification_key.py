# Generated by Django 4.2.1 on 2023-07-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.CharField(default='Не верифицирован', verbose_name='Ключ активации'),
        ),
    ]
