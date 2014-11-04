# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCountry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressRegion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='claims.AddressCountry')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimComment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('name', models.CharField(max_length=1023)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('name', models.CharField(max_length=1023)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAcl',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('project', models.ForeignKey(to='claims.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectField',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPieceHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', db_index=True, blank=True, editable=False)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('nick', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('city', models.ForeignKey(to='claims.AddressCity')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subscription',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypiecehistory',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypiecehistory',
            name='story_piece',
            field=models.ForeignKey(to='claims.StoryPiece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypiece',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypiece',
            name='obj',
            field=models.ForeignKey(to='claims.Object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectfield',
            name='project_field_group',
            field=models.ForeignKey(blank=True, to='claims.ProjectFieldGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objecthistory',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objecthistory',
            name='obj',
            field=models.ForeignKey(to='claims.Object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='object',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='object',
            name='project',
            field=models.ForeignKey(to='claims.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claimhistory',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claimhistory',
            name='claim',
            field=models.ForeignKey(to='claims.Claim'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claimcomment',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claimcomment',
            name='claim',
            field=models.ForeignKey(to='claims.Claim'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claim',
            name='author',
            field=models.ForeignKey(related_name='+', to='claims.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claim',
            name='obj',
            field=models.ForeignKey(to='claims.Object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addresscity',
            name='region',
            field=models.ForeignKey(to='claims.AddressRegion'),
            preserve_default=True,
        ),
    ]
