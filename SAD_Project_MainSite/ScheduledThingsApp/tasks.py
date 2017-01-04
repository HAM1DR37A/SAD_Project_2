# from celery import Celery
#
#
# # backend ==> vase inke javab ro tahvil begirim, broker ==> lazeme kolan ==> har joftesh ba rabitMQ
# app = Celery('tasks', backend='rpc://', broker='amqp://localhost')
# # For redis ==> broker=redis://localhost && backend='redis://localhost'
#
# app.conf.task_serializer = 'json'
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )
#
#
# # app.config_from_object('celeryconfig')    ===> az file ham mishe in app ro config kard ;) ==> celeryconfig.py
#
#
# @app.task
# def add(x, y):
#     return x + y


# =======================

from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')


# Way 1
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )
# Way 2
# app.conf.beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'tasks.test',
#         'schedule': 10.0,
#         'args': ('h')
#     },
# }
app.conf.timezone = 'UTC'


@app.task
def test(arg):
    print(arg)



# Way3
# myapp/tasks.py
# import datetime
# import celery
#
# @celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
# def myfunc():
#     print ('periodic_task')