# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='state',
        ),
        migrations.RemoveField(
            model_name='building',
            name='zip',
        ),
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.ForeignKey(to='core.Address'),
        ),
    ]
