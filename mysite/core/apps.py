from django.apps import AppConfig
import threading

import time, datetime
import schedule
from stock.strategy import *

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'mysite.core'

    def ready(self):
        # from jobs.updater import startSchedule
        def startSchedule():

            # scheduleJobTest = ScheduleJobTest()
            # schedule.every(3).seconds.do( scheduleJobTest.process )

            traderSellStock = TraderSellStock()
            schedule.every(10).seconds.do( traderSellStock.process )

            while True:
                schedule.run_pending()
                time.sleep(1)

        x = threading.Thread(target= startSchedule) # async
        # x.start()

class ScheduleJobTest:
    def __init__(self):
        print("ScheduleJobTest")

    def process(self):
        print("\n job",datetime.now())
     