# Generated by Django 3.0.2 on 2020-02-05 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200204_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 9, 43, 3, 578763)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 9, 43, 3, 584744)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 9, 43, 3, 582750)),
        ),
    ]
