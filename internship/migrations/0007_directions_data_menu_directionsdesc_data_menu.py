# Generated by Django 4.1.7 on 2023-04-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_alter_directions_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='directions',
            name='data_menu',
            field=models.CharField(default=1, max_length=200, verbose_name='data_menu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='directionsdesc',
            name='data_menu',
            field=models.CharField(default=1, max_length=200, verbose_name='data_menu'),
            preserve_default=False,
        ),
    ]
