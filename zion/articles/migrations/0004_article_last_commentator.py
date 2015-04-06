# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_article_last_commentator_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_commentator',
            field=models.ForeignKey(related_name='last_commentator', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
