# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_auto_20141115_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectacl',
            name='can_change_project_properties',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectacl',
            name='can_grant_acl',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
