# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_sidebar'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(default='', blank=True),
        ),
    ]
