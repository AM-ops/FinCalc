# Generated by Django 3.1 on 2020-10-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0003_auto_20201010_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='aetonp',
            name='type',
            field=models.CharField(default='Annual Effective to Nominal Per Period', max_length=25),
        ),
    ]
