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
    sender.add_periodic_task(10.0, test.s(), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s(), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s(),
    )

app.conf.timezone = 'UTC'


import requests
import time
import smtplib
from email.mime.text import MIMEText
@app.task
def test():
    print("Daily task is started")
    secretKey = "justShowMeTheBirthDay"
    url = "http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/"

    req = requests.get(url+secretKey)
    if(req.status_code != 200):
        print("right now the server is down")
        # time.sleep(60*5)  # delays for 5 minutes
        # test()
        return

    json = req.json()

    for x in range(len(json)):
        print(json[x]['birth_date'])
        msg = MIMEText("Dear "+json[x]['name']+json[x]['last_name']+"\n"+
                       "tavalodet mobarak \n"
                       "ZELIG TEAM")
        msg['Subject'] = 'Happy Birth Day '+json[x]['name']
        msg['From'] = 'sina@zelig.com'
        msg['To'] = 'yourmail@biNam.com'

        # SENDING MAIL FORMAT FOR ONLINE SMTP SERVER
        # server = smtplib.SMTP(smtpserver)
        # server.starttls()
        # server.login(login,password)
        # problems = server.sendmail(from_addr, to_addr_list, message)
        # server.quit()

        try:
            s = smtplib.SMTP('localhost:10000')
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
        except:
            print("Mail Server is down")
