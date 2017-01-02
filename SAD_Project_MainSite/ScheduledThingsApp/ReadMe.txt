http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

TODO we need a file which should contain the people whom today is their birth day
TODO baadan bebin chetour mishe bishtar in celery task ro ba Django ertebatesh dad

packages that should be installed:
sqlalchemy>=1.0.14
celery>=4.0

to use this first we need to run rabbitMQ-server

then we need to run celery worker using this command in this folder:
celery -A tasks worker -B --loglevel=info

all our scheduled tasks should be writen in tasks.py






FAQ:
for killing rabbitMQ
$: ps aux | grep epmd
$: ps aux | grep erl
