# Generated by Django 3.1 on 2020-10-12 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0010_auto_20201012_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aetonp',
            name='user',
        ),
    ]