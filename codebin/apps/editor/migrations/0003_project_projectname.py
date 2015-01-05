# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_project_projectpublic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectName',
            field=models.CharField(default='name', max_length=40),
            preserve_default=True,
        ),
    ]
