# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_last_commentator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='last_commentator_avatar',
        ),
    ]
