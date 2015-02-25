# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0002_chromosome_scaffold_sequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scaffold',
            name='end',
        ),
        migrations.RemoveField(
            model_name='scaffold',
            name='start',
        ),
    ]
