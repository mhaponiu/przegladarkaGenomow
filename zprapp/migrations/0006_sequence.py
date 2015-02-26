# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0005_auto_20150225_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.TextField()),
                ('scaffold', models.ForeignKey(to='zprapp.Scaffold')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
