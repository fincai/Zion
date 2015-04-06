# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0003_remove_forum_last_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='last_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forum',
            name='last_postdate',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
