# Generated by Django 4.2.7 on 2023-11-07 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_remove_habit_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='subscribed_to_bot',
        ),
    ]
