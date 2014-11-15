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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('nick', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('name', models.CharField(primary_key=True, max_length=255, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=1023)),
                ('external_uri', models.URLField(max_length=255)),
                ('description', models.TextField()),
                ('kogdaigra_link', jrlib.models.KogdaIgraField()),
                ('game_begin_date', models.DateField()),
                ('game_end_date', models.DateField()),
                ('vk_club', jrlib.models.VKField()),
                ('lj_comm', jrlib.models.LiveJournalField()),
                ('facebook', jrlib.models.FacebookField()),
                ('twitter', jrlib.models.TwitterField()),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('project_field', models.ForeignKey(to='claims.ProjectField')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True, help_text='Может ли мастер менять что-то в проекте или он уже ушел в архив')),
                ('is_visible', models.BooleanField(default=False, help_text='Может ли игрок увидеть проект во всяких «куда заявиться»')),
                ('can_add_new_claim', models.BooleanField(default=False, help_text='Могут ли игроки добавлять новые заявки или они закрыты (уже/еще)')),
                ('can_player_change_character', models.BooleanField(default=False, help_text='Могут ли игроки что-то менять в персонаже или мастера заморозили заявки к выезду на полигон')),
            ],
            options={
                'verbose_name': 'Статус проектов',
                'verbose_name_plural': 'Статусы проектов',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guid', django_extensions.db.fields.UUIDField(blank=True, db_index=True, editable=False, name='guid')),
                ('cr_date', django_extensions.db.fields.CreationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('up_date', django_extensions.db.fields.ModificationDateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
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
            field=models.ForeignKey(blank=True, to='claims.ProjectFieldGroup', null=True),
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
            field=models.ForeignKey(blank=True, to='claims.AddressCity', null=True),
            preserve_default=True,
        ),
    ]
