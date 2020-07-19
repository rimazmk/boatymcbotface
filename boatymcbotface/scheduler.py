import schedule
from .messaging import send_picture
import threading


def job():
    print("running job")
    send_picture("bottesting")


def run_job():
    schedule.every().day.at("18:00").do(job)
    while True:
        schedule.run_pending()


t = threading.Thread(target=run_job)
t.daemon = True
t.start()
