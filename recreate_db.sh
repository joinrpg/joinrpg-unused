#!/bin/bash
set -e

rm -f claims/migrations/0001_initial.py
rm -f db.sqlite3

DIR=`mktemp -d /tmp/joinrpg.migrate.XXXXXX`
mv claims/migrations/*.py $DIR/
mv $DIR/__init__.py claims/migrations/

python manage.py makemigrations claims

mv $DIR/*.py claims/migrations/
rm -rf $DIR


python manage.py migrate
python manage.py createsuperuser
