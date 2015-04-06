# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_last_commentator_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_commentator',
            field=models.ForeignKey(related_name='last_commentator', null=True, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
