# Generated by Django 2.2.1 on 2019-06-03 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190530_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
