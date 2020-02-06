# Generated by Django 3.0.1 on 2020-02-05 18:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200206_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 6, 57, 480968)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 6, 57, 484505)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 6, 57, 483504)),
        ),
        migrations.RemoveField(
            model_name='public',
            name='post',
        ),
        migrations.AddField(
            model_name='public',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.idea'),
        ),
    ]
