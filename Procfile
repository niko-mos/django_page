release: python manage.py migrate
web: gunicorn cosmologia.wsgi:application
heroku ps: scale worker=1