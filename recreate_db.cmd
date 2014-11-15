@echo off
rem removing db
del db.sqlite3
rem removing intial migration
del claims\migrations\0001_initial.py
rem removing temporary dir, if left
rmdir temp.migrate /q /s
rem storing migrations except 1st
md temp.migrate
move claims\migrations\*.py temp.migrate\
move temp.migrate\__init__.py claims\migrations

rem create migrations
python manage.py makemigrations claims

move temp.migrate\*.py claims\migrations\

rmdir temp.migrate /q /s

python manage.py migrate
python manage.py createsuperuser