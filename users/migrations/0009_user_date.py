# Generated by Django 4.1.7 on 2023-04-08 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_mail_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]