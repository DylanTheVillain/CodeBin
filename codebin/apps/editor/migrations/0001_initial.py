# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forked',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('forkedParentHash', models.CharField(max_length=40)),
                ('forkedHash', models.CharField(max_length=40)),
                ('forkedDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('projectCode', models.TextField()),
                ('projectCreationDate', models.DateTimeField(auto_now_add=True)),
                ('projectLastUpdate', models.DateTimeField(auto_now=True)),
                ('projectHash', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
