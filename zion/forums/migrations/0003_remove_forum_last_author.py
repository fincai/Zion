# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_forum_last_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='last_author',
        ),
    ]
