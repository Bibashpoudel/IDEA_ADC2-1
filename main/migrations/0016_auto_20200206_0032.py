# Generated by Django 3.0.1 on 2020-02-05 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200206_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 32, 18, 907382)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 32, 18, 911374)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 0, 32, 18, 910502)),
        ),
    ]