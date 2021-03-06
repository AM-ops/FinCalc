# Generated by Django 3.1 on 2020-11-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0031_ctonp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aetoc',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoc',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoc',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoep',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoep',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoep',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetoep',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetonp',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetonp',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetonp',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='aetonp',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoae',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoae',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoae',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoep',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoep',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoep',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctoep',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctonp',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctonp',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctonp',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='ctonp',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoae',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoae',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoae',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoae',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoc',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoc',
            name='i',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoc',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoc',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoep',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoep',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoep',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoep',
            name='pone',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptoep',
            name='ptwo',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptonp',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptonp',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptonp',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptonp',
            name='pone',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='eptonp',
            name='ptwo',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoae',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoae',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoae',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoae',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoc',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoc',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoc',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoc',
            name='p',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoep',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoep',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoep',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoep',
            name='pone',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptoep',
            name='ptwo',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptonp',
            name='answer',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptonp',
            name='idiv',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptonp',
            name='ip',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptonp',
            name='pone',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='nptonp',
            name='ptwo',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
    ]
