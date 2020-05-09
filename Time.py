from telegram.ext import Updater, CommandHandler
import schedule
import threading
import time
import Commands
command=Commands.Commands()
class Time: 
    #schedule.every().hour.do(command.get_currencies)
    schedule.every().day.at("16:30").do(command.get_currencies)

    while True:
       schedule.run_pending()
       time.sleep(1)