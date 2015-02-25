# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chromosome',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('length', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scaffold',
            fields=[
                ('id', models.TextField(unique=True, serialize=False, primary_key=True)),
                ('length', models.FloatField()),
                ('order', models.IntegerField()),
                ('start', models.FloatField()),
                ('end', models.FloatField()),
                ('chromosome', models.ForeignKey(to='zprapp.Chromosome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
