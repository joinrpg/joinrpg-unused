# -*- coding: utf-8 -*-

from django.db import models
from django_extensions.db.fields import UUIDField

# Специальный маленький класс, чтобы у нас везде попали GUID'ы

class JRModel(models.Model):
    guid = UUIDField(db_index=True)

    class Meta:
        abstract = True
       
