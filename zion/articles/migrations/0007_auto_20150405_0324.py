# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150405_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_commentator',
            field=models.OneToOneField(related_name='last_commentator', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
