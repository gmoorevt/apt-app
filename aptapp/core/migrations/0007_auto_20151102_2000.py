# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151027_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='security_dep',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
