# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import jrlib.models
from django.conf import settings
import jsonfield.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('nick', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='claims.AddressCountry')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthenticationSystem',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('name', models.CharField(serialize=False, max_length=255, primary_key=True)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('claim', models.ForeignKey(to='claims.Claim')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('claim', models.ForeignKey(to='claims.Claim')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('name', models.CharField(max_length=1023)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('obj', models.ForeignKey(to='claims.Object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('name', models.CharField(max_length=1023)),
                ('external_uri', models.URLField(max_length=255)),
                ('description', models.TextField()),
                ('vk_club', jrlib.models.VKField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAcl',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('project', models.ForeignKey(to='claims.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectField',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('project', models.ForeignKey(to='claims.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFieldGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('project', models.ForeignKey(to='claims.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('project_field', models.ForeignKey(to='claims.ProjectField')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('obj', models.ForeignKey(to='claims.Object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPieceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('story_piece', models.ForeignKey(to='claims.StoryPiece')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, name='guid', editable=False, blank=True)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(editable=False, default=django.utils.timezone.now, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectfield',
            name='project_field_group',
            field=models.ForeignKey(null=True, to='claims.ProjectFieldGroup', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='object',
            name='project',
            field=models.ForeignKey(to='claims.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claim',
            name='obj',
            field=models.ForeignKey(to='claims.Object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authentication',
            name='system',
            field=models.ForeignKey(to='claims.AuthenticationSystem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authentication',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addresscity',
            name='region',
            field=models.ForeignKey(to='claims.AddressRegion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, to='claims.AddressCity', blank=True),
            preserve_default=True,
        ),
    ]
