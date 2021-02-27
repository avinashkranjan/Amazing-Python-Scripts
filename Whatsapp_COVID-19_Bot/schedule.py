# Imports

from apscheduler.schedulers.blocking import BlockingScheduler
from covid_bot import *

scheduler = BlockingScheduler()


def bot_schedule():
    """
    A scheduler for the covid_bot script
    """
    for numb in receiver_list:
        print(f"sending message to {numb}")
        send_message(numb, messages)


# The Job is scheduled for once a day.
# The event is triggered at 5:30AM IST (Midnight UTC)
scheduler.add_job(bot_schedule, 'cron', days='*/1')
scheduler.start()
