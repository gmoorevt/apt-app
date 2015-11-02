# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151027_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, 'Permeate'), (2, 'Work'), (3, 'Apartment')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=12),
        ),
    ]
