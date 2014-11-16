# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_authentication_systems(apps, schema_editor):
    AuthenticationSystem = apps.get_model("claims", "AuthenticationSystem")
    a = AuthenticationSystem(name="local", data="{}")
    a.save()

def add_project_statuses(apps, schema_editor):
    ProjectStatus = apps.get_model("claims", "ProjectStatus")
    ProjectStatus(name="Новый проект (заявки не открыты)", is_active=True, is_visible=False, can_add_new_claim=False, can_player_change_character=False, is_default_status=True).save()
    ProjectStatus(name="Заявки открыты", is_active=True, is_visible=True, can_add_new_claim=True, can_player_change_character=True).save()
    ProjectStatus(name="Новые заявки не принимаются", is_active=True, is_visible=True, can_add_new_claim=False, can_player_change_character=True).save()
    ProjectStatus(name="Отъезд на полигон (менять заявки нельзя)", is_active=True, is_visible=True, can_add_new_claim=False, can_player_change_character=False).save()
    ProjectStatus(name="Проект в архиве", is_active=True, is_visible=False, can_add_new_claim=False, can_player_change_character=False).save()
    
    
class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_authentication_systems),
        migrations.RunPython(add_project_statuses),
    ]
