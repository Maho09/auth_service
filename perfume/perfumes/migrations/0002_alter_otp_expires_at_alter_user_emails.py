# Generated by Django 5.0.6 on 2024-07-08 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 16, 33, 15, 897148, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='emails',
            field=models.BooleanField(default=False),
        ),
    ]