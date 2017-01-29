from __future__ import absolute_import
import celery

@celery.task
def add(x, y):
    return x + y