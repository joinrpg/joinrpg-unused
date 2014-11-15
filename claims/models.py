# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField
from jrlib.models import JRModel

# Адрес
class AddressCountry(JRModel):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class AddressRegion(JRModel):
    country = models.ForeignKey(AddressCountry)
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class AddressCity(JRModel):
    region = models.ForeignKey(AddressRegion)
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

# Пользователь
class User(JRModel):
    city = models.ForeignKey(AddressCity)

    first_name = models.CharField(max_length = 255)
    second_name =  models.CharField(max_length = 255)
    nick = models.CharField(max_length = 255)
    email = models.EmailField()

# Базовый класс (без создания таблицы) для любых "авторских" 
# таблиц, т.е., у записей которых есть автор из Users

class AuthoredModel(JRModel):
    author = models.ForeignKey(User, related_name='+')
    cr_date = CreationDateTimeField()
    up_date = ModificationDateTimeField()

    class Meta:
        abstract = True


# проект — собсно, игра
class Project(AuthoredModel):
    name = models.CharField(max_length = 1023)
    # TODO

# Права доступа к проекту
class ProjectAcl(JRModel):
    project = models.ForeignKey(Project)

# Группы полей заявок в проекте
class ProjectFieldGroup(JRModel):
    project = models.ForeignKey(Project)

# Поля заявки в проекте
class ProjectField(JRModel):
    project = models.ForeignKey(Project)
    project_field_group = models.ForeignKey(ProjectFieldGroup, blank=True, null=True)

# Значения комбобоксов в полях заявок в проекте
class ProjectFieldValue(JRModel):
    project_field = models.ForeignKey(ProjectField)

# Объекты игрового мира — персонажики, группочки персонажиков, локации
class Object(AuthoredModel):
    project = models.ForeignKey(Project)

    name = models.CharField(max_length=1023)

# История изменений в объектах
class ObjectHistory(AuthoredModel):
    obj = models.ForeignKey(Object)

# Подписки пользователей на изменения
class Subscription(AuthoredModel):
    user = models.ForeignKey(User)
    # TODO

# Заявка
class Claim(AuthoredModel):
    obj = models.ForeignKey(Object)

# история изменения заявок
class ClaimHistory(AuthoredModel):
    claim = models.ForeignKey(Claim)

# Комментарии к заявке (переписка)
class ClaimComment(AuthoredModel):
    claim = models.ForeignKey(Claim)

# Загрузы
class StoryPiece(AuthoredModel):
    obj = models.ForeignKey(Object)

# История изменения загрузов
class StoryPieceHistory(AuthoredModel):
    story_piece = models.ForeignKey(StoryPiece)


