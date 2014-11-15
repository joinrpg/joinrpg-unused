# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_authentication_systems(apps, schema_editor):
    AuthenticationSystem = apps.get_model("claims", "AuthenticationSystem")
    a = AuthenticationSystem(name="local", data="{}")
    a.save()

class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_authentication_systems),
    ]
