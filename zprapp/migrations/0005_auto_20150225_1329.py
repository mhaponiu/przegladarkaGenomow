# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0004_auto_20150225_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='scaffold',
        ),
        migrations.DeleteModel(
            name='Sequence',
        ),
    ]
