# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=12)),
                ('type', models.IntegerField(choices=[('1', 'Permeate'), ('2', 'Work'), ('3', 'Apartment')])),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('security_dep', models.DateField()),
                ('rent_amount', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('payment_date', models.DateField()),
                ('description', models.TextField()),
                ('lease', models.ForeignKey(to='core.Lease')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Receivable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('due_date', models.DateField()),
                ('description', models.TextField()),
                ('lease', models.ForeignKey(to='core.Lease')),
                ('payment', models.ForeignKey(to='core.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=20)),
                ('cell_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('number_bedrooms', models.IntegerField()),
                ('number_bathrooms', models.IntegerField()),
                ('building', models.ForeignKey(to='core.Building')),
            ],
        ),
        migrations.AddField(
            model_name='receivable',
            name='tenant',
            field=models.ForeignKey(to='core.Tenant'),
        ),
        migrations.AddField(
            model_name='payment',
            name='tenant',
            field=models.ForeignKey(to='core.Tenant'),
        ),
        migrations.AddField(
            model_name='lease',
            name='tenant',
            field=models.ForeignKey(to='core.Tenant'),
        ),
        migrations.AddField(
            model_name='building',
            name='portfolio',
            field=models.ForeignKey(to='core.Portfolio'),
        ),
    ]
