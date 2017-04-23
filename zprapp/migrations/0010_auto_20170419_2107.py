# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-19 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zprapp', '0009_auto_20170419_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='chromosome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='zprapp.Chromosome'),
        ),
    ]