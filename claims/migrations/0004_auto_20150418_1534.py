# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jrlib.models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_auto_20141116_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfield',
            name='name',
            field=models.CharField(verbose_name='Имя поля', default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectfield',
            name='order',
            field=jrlib.models.OrderField(verbose_name='Порядок', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectfield',
            name='type',
            field=models.PositiveSmallIntegerField(verbose_name='Тип поля', choices=[(1, 'Текстовое поле')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectfieldgroup',
            name='description',
            field=models.TextField(verbose_name='Описание группы полей', default='', max_length=1023),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectfieldgroup',
            name='name',
            field=models.CharField(verbose_name='Название группы полей', default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectfieldgroup',
            name='order',
            field=jrlib.models.OrderField(verbose_name='Порядок', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectfield',
            name='project_field_group',
            field=models.ForeignKey(to='claims.ProjectFieldGroup'),
            preserve_default=True,
        ),
    ]
