from celery import Celery
from celery.schedules import crontab

import requests
import time
import smtplib
from email.mime.text import MIMEText
import datetime

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')
app.conf.timezone = 'UTC'


@app.task
def send_hpd_msg():
    print("Daily task is started")
    secret_key = "justShowMeTheBirthDay"
    url = "http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/"

    req = requests.get(url+secret_key)
    if req.status_code != 200 :
        print("right now the server is down")
        # time.sleep(60*5)  # delays for 5 minutes
        # send_hpd_msg()
        return

    json = req.json()
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')

    for x in range(len(json)):
        if today_date == json[x]['birth_date']:
            msg = MIMEText("Dear "+json[x]['name']+" "+json[x]['last_name']+"\n"+
                           "tavalodet mobarak \n\n"
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
                print("Tabrik msg was sent to "+json[x]['name'])
            except:
                print("Mail Server is down")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls send_hpd_msg() every 10 seconds ==> just for testing
    sender.add_periodic_task(10.0, send_hpd_msg.s(), name='add every 10')

    # Executes every morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30),
        send_hpd_msg.s(),
    )

