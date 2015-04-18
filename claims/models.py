# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField
from jrlib.models import *
import jsonfield
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django_extensions.db.fields import UUIDField

# UserManager

class UserManager(BaseUserManager):
    def __create_user(self, username, is_su=False, password=None):
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(username=username)
        user.is_superuser = is_su
        user.save()
        if password:
            auth_sys = AuthenticationSystem.objects.get(name='local')
            if not auth_sys:
                raise ValueError('There are no \'local\' Authentication system. Please create one first')
            auth = Authentication.objects.create(user=user, system=auth_sys, data = {'password': password})
            auth.save()
        
    def create_user(self, username, password=None):
        self.__create_user(username, False, password)

    def create_superuser(self, username, password):
        if not password:
            raise ValueError('Superuser MUST have a password')
        self.__create_user(username, True, password)
        
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
class User(AbstractBaseUser):
    guid = UUIDField(db_index=True)
    city = models.ForeignKey(AddressCity, null=True)

    first_name = models.CharField(null=True, max_length = 255)
    second_name = models.CharField(null=True, max_length = 255)
    patronymic = models.CharField(null=True, max_length = 255)
    nick = models.CharField(null=True, max_length = 255)
    
    email = models.EmailField(null=True)
    username = models.CharField(unique=True, max_length = 42)

    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_admin(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.username
        
#    last_login = models.DateTimeField(auto_now_add=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def check_password(self, raw_password):
        try:
            auth = Authentication.objects.get(user=self, system='local')
        except Authentication.DoesNotExist:
            auth = None

        if auth is None:
            return False
        return auth.data['password'] == raw_password

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
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class ProjectStatus(JRModel):
    name = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True, help_text='Может ли мастер менять что-то в проекте или он уже ушел в архив')
    is_visible = models.BooleanField(default=False, help_text='Может ли игрок увидеть проект во всяких «куда заявиться»') 
    can_add_new_claim = models.BooleanField(default=False, help_text='Могут ли игроки добавлять новые заявки или они закрыты (уже/еще)') 
    can_player_change_character = models.BooleanField(default=False, help_text='Могут ли игроки что-то менять в персонаже или мастера заморозили заявки к выезду на полигон')
    is_default_status = models.BooleanField('Статус для вновь созданных игр', default=False, help_text='Да, если этот статус выставляется проекту при создании')
    
    class Meta:
        verbose_name = "Статус проектов"
        verbose_name_plural = "Статусы проектов"
    def __str__(self):
        return self.name

# проект — собсно, игра
class Project(AuthoredModel):
    name = models.CharField('Название игры (проекта)', max_length = 1023)
    external_uri = models.URLField('Сссылка на сайт игры', max_length = 255, null=True, blank=True)
    description = models.TextField('Описание игры (для игроков)', null=True, blank=True)
    kogdaigra_link = KogdaIgraField('Ссылка на профиль на КогдаИгре', null=True, blank=True)
    game_begin_date = models.DateField('Дата начала игры')
    game_end_date = models.DateField('Дата конца игры')
    status = models.ForeignKey(ProjectStatus, verbose_name='Статус проекта')
    
    #project social networks
    vk_club = VKField(null=True)
    lj_comm = LiveJournalField(null=True, blank=True)
    facebook = FacebookField(null=True, blank=True)
    twitter = TwitterField(null=True, blank=True)
    
    # TODO

# Права доступа к проекту
class ProjectAcl(JRModel):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
        
    can_change_player_fields = models.BooleanField(default=True)
    can_write_comments = models.BooleanField(default=True)
    can_accept_money = models.BooleanField(default=True)
    can_setup_fields = models.BooleanField(default=False)
    can_grant_acl = models.BooleanField(default=False)
    can_change_project_properties = models.BooleanField(default=False)
    
    @staticmethod
    def create_author_fullcontrol(project):
        self = ProjectAcl()
        self.project = project
        self.user = project.author
        self.can_change_player_fields = True
        self.can_write_comments = True
        self.can_accept_money = True
        self.can_setup_fields = True
        self.can_grant_acl = True
        self.can_change_project_properties = True
        return self
        

# Группы полей заявок в проекте
class ProjectFieldGroup(JRModel):
    project = models.ForeignKey(Project)
    name = models.CharField('Название группы полей', max_length=255)
    order = OrderField('Порядок')
    description = models.TextField('Описание группы полей', max_length=1023)

class ProjectFieldTypeImpl:
    def __init__ (self, id, name):
        self.id = id
        self.name = name
    
    def as_choice(self):
        return (self.id, self.name)
            
# Поля заявки в проекте
class ProjectField(JRModel):
    TYPE_TEXT = ProjectFieldTypeImpl(1, 'Текстовое поле')
    
    ALL_TYPES = [TYPE_TEXT]
    
    project = models.ForeignKey(Project)
    project_field_group = models.ForeignKey(ProjectFieldGroup)
    
    name = models.CharField('Имя поля', max_length=255)
    order = OrderField('Порядок')
    type = models.PositiveSmallIntegerField('Тип поля', choices = map (lambda x: x.as_choice(), ALL_TYPES))
    
    def get_type(self):
        return next(x for x in ALL_TYPES if x.id == self.type)
    
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


