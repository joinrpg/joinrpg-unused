#!/bin/bash
set -e
set -x
rm -f claims/migrations/0001_initial.py
rm -f db.sqlite3

DIR=`mktemp -d /tmp/joinrpg.migrate.XXXXXX`
mv claims/migrations/*.py $DIR/
mv $DIR/__init__.py claims/migrations/

FAIL="NO"

python manage.py makemigrations claims || FAIL="YES"

mv $DIR/*.py claims/migrations/
rm -rf $DIR

if [ $FAIL == "NO" ]; then
    python manage.py migrate || FAIL="YES"
fi

if [ $FAIL == "NO" ]; then
    python manage.py createsuperuser
fi
