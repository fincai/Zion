# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_collected_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='agreed_users',
            field=models.ManyToManyField(related_name='posted_articles', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='collected_users',
            field=models.ManyToManyField(related_name='collected_articles', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
