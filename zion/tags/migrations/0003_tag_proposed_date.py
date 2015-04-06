# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20150405_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='proposed_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
