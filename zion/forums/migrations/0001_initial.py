# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('articles', models.PositiveIntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'forum',
            },
            bases=(models.Model,),
        ),
    ]
