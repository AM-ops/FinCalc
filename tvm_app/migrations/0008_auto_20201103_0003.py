# Generated by Django 3.1 on 2020-11-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvm_app', '0007_consannuarrav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consannuarrav',
            name='type',
            field=models.CharField(default='AV for Constant Annuity paid in arrears', max_length=50),
        ),
    ]
