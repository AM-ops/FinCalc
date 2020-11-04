# Generated by Django 3.1 on 2020-11-03 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tvm_app', '0010_consannupv'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncAnnuArrAV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.DecimalField(decimal_places=5, max_digits=10)),
                ('i', models.DecimalField(decimal_places=5, max_digits=10)),
                ('j', models.DecimalField(decimal_places=5, max_digits=10)),
                ('n', models.DecimalField(decimal_places=5, max_digits=10)),
                ('x', models.DecimalField(decimal_places=5, max_digits=10)),
                ('idiv', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('jdiv', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('answer', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('description', models.CharField(default='', max_length=50)),
                ('type', models.CharField(default='AV for Increasing Annuity with Interest Paid in Advance', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
