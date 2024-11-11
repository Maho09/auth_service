# Generated by Django 5.0.6 on 2024-08-02 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0003_user_attempts_alter_otp_expires_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders_count',
        ),
        migrations.AddField(
            model_name='user',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 13, 48, 4, 257149, tzinfo=datetime.timezone.utc)),
        ),
    ]
