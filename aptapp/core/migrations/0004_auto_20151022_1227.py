# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_address_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(default=1, max_length=10, choices=[('1', 'Permeate'), ('2', 'Work'), ('3', 'Apartment')]),
        ),
    ]
