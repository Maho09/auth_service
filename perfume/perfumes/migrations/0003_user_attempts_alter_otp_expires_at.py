# Generated by Django 5.0.6 on 2024-07-15 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0002_alter_otp_expires_at_alter_user_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 20, 31, 32, 15433, tzinfo=datetime.timezone.utc)),
        ),
    ]
