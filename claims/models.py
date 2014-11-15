# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField
from jrlib.models import *
import jsonfield
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# UserManager

class UserManager(BaseUserManager):
    def __create_user(self, email, is_su=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=email)
        user.is_superuser = is_su
        user.save()
        if password:
            auth_sys = AuthenticationSystem.objects.get(name='local')
            if not auth_sys:
                raise ValueError('There are no \'local\' Authentication system. Please create one first')
            auth = Authentication.objects.create(user=user, system=auth_sys, data = {'password': password})
            auth.save()
        
    def create_user(self, email, password=None):
        self.__create_user(email, False, password)

    def create_superuser(self, email, password):
        if not password:
            raise ValueError('Superuser MUST have a password')
        self.__create_user(email, True, password)
        
# Адрес
class AddressCountry(JRModel):
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
    def __str__(self):
        return self.name

class AddressRegion(JRModel):
    country = models.ForeignKey(AddressCountry)
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
    def __str__(self):
        return self.name

class AddressCity(JRModel):
    region = models.ForeignKey(AddressRegion)
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
    def __str__(self):
        return self.name

# Пользователь
class User(JRModel):
    city = models.ForeignKey(AddressCity, blank=True, null=True)

    first_name = models.CharField(max_length = 255)
    second_name = models.CharField(max_length = 255)
    nick = models.CharField(max_length = 255)
    
    email = models.EmailField(unique=True)

    cr_date = CreationDateTimeField()
    up_date = ModificationDateTimeField()
    active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class AuthenticationSystem(JRModel):
    name = models.CharField(primary_key = True, max_length = 255)
    data = jsonfield.JSONField()

class Authentication(JRModel):
    user = models.ForeignKey(User, related_name='+')
    system = models.ForeignKey(AuthenticationSystem)
    data = jsonfield.JSONField()

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
    external_uri = models.URLField(max_length = 255)
    description = models.TextField()
    
    #project social networks
    vk_club = VKField()
    lj_comm = LiveJournalField()
    facebook = FacebookField()
    twitter = TwitterField()
    
    # TODO

# Права доступа к проекту
class ProjectAcl(JRModel):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)

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


