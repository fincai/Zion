# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20150405_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=255)),
                ('article_count', models.PositiveIntegerField(default=0)),
                ('articles', models.ManyToManyField(related_name='articles', to='articles.Article')),
            ],
            options={
                'db_table': 'tag',
            },
            bases=(models.Model,),
        ),
    ]
