# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_auto_20150405_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='last_author',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
