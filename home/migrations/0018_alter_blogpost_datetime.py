# Generated by Django 4.2.1 on 2024-01-20 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_comment_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
