# Generated by Django 3.1 on 2020-10-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0005_auto_20201010_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='aetonp',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]
