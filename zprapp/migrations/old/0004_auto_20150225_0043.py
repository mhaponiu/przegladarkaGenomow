# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0003_auto_20150224_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='id',
        ),
        migrations.AlterField(
            model_name='sequence',
            name='sequence',
            field=models.TextField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
