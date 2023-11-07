# Generated by Django 4.2.7 on 2023-11-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_subscribed_to_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_handle',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Telegram'),
        ),
    ]
