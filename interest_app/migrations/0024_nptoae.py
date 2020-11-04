# Generated by Django 3.1 on 2020-10-17 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interest_app', '0023_eptoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPtoAE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ip', models.DecimalField(decimal_places=5, max_digits=10)),
                ('idiv', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('answer', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('description', models.CharField(default='', max_length=50)),
                ('type', models.CharField(default='Nominal Per Period to Annual Effective Rate', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
