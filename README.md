joinrpg
=======

JoinRPG.ru Python/Django sources

*_This file is in UTF-8 Russian_*

(_Владимир "Даир" Лебедев-Шмидтгоф, 5 Ноября 2014_)

# Как запустить проект

* Установить Python 3
  * Для Windows https://www.python.org/downloads/
  * При установке python выбрать «добавить python в path»
  * Если на компьютере уже установлена версия Python 2.x и её необходимо сохранить, то воспользуйтесь каким-нибудь методом, описанным здесь: http://stackoverflow.com/questions/3809314/how-to-install-both-python-2-x-and-python-3-x-in-windows-7
* Установить Git. 
  * Если вы не умеете в Git и хотите быстрый вариант для Windows, вот он https://windows.github.com/
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

# Сервер beta.joinrpg.ru

Сервер `beta.joinrpg.ru` автоматом подхватывает изменения в бранче `develop`.
Чтобы увидеть изменения, можно сходить по ссылкам
* http://beta.joinrpg.ru/claims/
* http://beta.joinrpg.ru/admin/

На сервере не исполняется автоматически `migrate` (т.е. не обновляется структура БД, если она были изменена) и не доставляются пререквизиты (`pip install`). Об этом баг #31

# Откуда брать задачи для работы

Текущий milestone/итерация называется 0.1 Все задачи по этой итерации лежат здесь https://github.com/joinrpg/joinrpg/milestones/V0.1

Задачи, которые не назначены ни на кого — здесь https://github.com/joinrpg/joinrpg/issues?q=is%3Aopen+milestone%3AV0.1+no%3Aassignee
