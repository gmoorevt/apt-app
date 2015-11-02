# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151022_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='none', max_length=2),
            preserve_default=False,
        ),
    ]
