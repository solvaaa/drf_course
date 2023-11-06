# Generated by Django 4.2.7 on 2023-11-06 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('habits', '0003_alter_habit_duration_alter_habit_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='periodic_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask'),
        ),
        migrations.AddField(
            model_name='habit',
            name='subscribed_to_bot',
            field=models.BooleanField(default=False, verbose_name='подписан на бота?'),
        ),
    ]
