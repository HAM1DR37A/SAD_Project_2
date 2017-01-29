from __future__ import absolute_import
from celery import Celery

celery = Celery(
    'tasks',
    broker='amqp://',
    backend='amqp',
    include=['tasks.py']
)

if __name__ == '__main__':
    celery.start()