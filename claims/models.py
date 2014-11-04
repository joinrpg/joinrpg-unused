# -*- coding: utf-8 -*-
from django.db import models

# Адрес
class AddressCountry(models.Model):
    name = models.CharField(max_length=255)

class AddressRegion(models.Model):
    country = models.ForeignKey(AddressCountry)
    pass

class AddressCity(models.Model):
    region = models.ForeignKey(AddressRegion)

# Пользователь
class User(models.Model):
    pass

# Заявка

class Claim(models.Model):
    pass

# история изменения заявок
class ClaimHistory(models.Model):
    pass

# Комментарии к заявке (переписка)
class ClaimComment(models.Model):
    pass

# Загрузы
class StoryPiece(models.Model):
    pass

# История изменения загрузов
class StoryPieceHistory(models.Model):
    pass

# Объекты игрового мира — персонажики, группочки персонажиков, локации
class Object(models.Model):
    pass

# История изменений в объектах
class ObjectHistory(models.Model):
    pass

# Подписки пользователей на изменения
class Subscription(models.Model):
    pass

# проект — собсно, игра
class Project(models.Model):
    pass

# Права доступа к проекту
class ProjectAcl(models.Model):
    pass

# Поля заявки в проекте
class ProjectField(models.Model):
    pass

# Группы полей заявок в проекте
class ProjectFieldGroup(models.Model):
    pass

# Значения комбобоксов в полях заявок в проекте
class ProjectFieldValue(models.Model):
    pass

