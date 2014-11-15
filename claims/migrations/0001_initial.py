# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import jrlib.models
import django_extensions.db.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('second_name', models.CharField(max_length=255, null=True)),
                ('patronymic', models.CharField(max_length=255, null=True)),
                ('nick', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('username', models.CharField(max_length=42, unique=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Города',
                'verbose_name': 'Город',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCountry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Страны',
                'verbose_name': 'Страна',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressRegion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='claims.AddressCountry')),
            ],
            options={
                'verbose_name_plural': 'Регионы',
                'verbose_name': 'Регион',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
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
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(serialize=False, primary_key=True, max_length=255)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1023)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1023)),
                ('external_uri', models.URLField(max_length=255)),
                ('description', models.TextField()),
                ('vk_club', jrlib.models.VKField()),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAcl',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
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
            field=models.ForeignKey(to='claims.ProjectFieldGroup', null=True, blank=True),
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
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(null=True, to='claims.AddressCity'),
            preserve_default=True,
        ),
    ]
