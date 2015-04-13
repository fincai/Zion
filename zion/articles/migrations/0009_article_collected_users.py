# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_auto_20150405_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='collected_users',
            field=models.ManyToManyField(related_name='collected_users', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
