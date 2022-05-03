#!/bin/bash
set -e
# python manage.py migrate --fake shirts
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput


# python manage.py shell -c "from users.models import User; User.objects.create_superuser('admin4', 'admin@example.com', '123qwe456asd')"


uwsgi --socket :8000 --master --enable-threads -b 32768 --module libratracking.wsgi 