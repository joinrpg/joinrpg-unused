joinrpg
=======

JoinRPG.ru Python/Django sources

*_This file is in UTF-8 Russian_*

(_Владимир "Даир" Лебедев-Шмидтгоф, 5 Ноября 2014_)

# Как запустить проект

* Установить Python 3
| * Для Windows https://www.python.org/downloads/
| * При установке python выбрать «добавить python в path»
* Установить Git. 
| * Если вы не умеете в Git и хотите быстрый вариант для Windows, вот он https://windows.github.com/
* Склонировать репозиторий в какой-нибудь каталог
* Открыть консоль в этом каталоге
* Установить Django и все необходимые пререквизиты
  * В консоли `pip install -r requirements.txt`
* После этого надо сгенерировать Базу Данных (один раз):
  * Запустить в каталоге, куда скачан репозиторий `python manage.py migrate`, от этого появится db.sqlite3 в корне проекта. Его *НЕ НАДО* добавлять в репозиторий (оно в `.gitignore` уже прописано)
  * Сгенерировать суперпользователя: `python manage.py createsuperuser`
* Теперь можно запускать проект:
  * `python manage.py runserver`
* После чего можно заходить (пока, правда, некуда) из броузера:
  * http://127.0.0.1:8000/

# Файл конфигурации

В корне лежит файл joinrpg.conf.sample, который, при необходимости развёртывания в условиях, близких к боевым, надо скопировать в joinrpg.conf и прописать там настройки базы. Этот файл внесён в `.gitignore`, его НЕ НАДО вносить в git.
