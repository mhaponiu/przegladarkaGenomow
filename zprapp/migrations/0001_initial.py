# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chromosome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('length', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('start', models.FloatField()),
                ('length', models.FloatField()),
                ('chromosome', models.ForeignKey(to='zprapp.Chromosome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mean', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
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
        migrations.AddField(
            model_name='marker',
            name='meaning',
            field=models.ForeignKey(to='zprapp.Meaning'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chromosome',
            name='organism',
            field=models.ForeignKey(to='zprapp.Organism'),
            preserve_default=True,
        ),
    ]
