from telegram.ext import Updater, CommandHandler
import schedule
import threading
import time
import Commands
command=Commands.Commands()
class Time: 
    def timer_start():
        threading.Timer(30.0, timer_start).start()
        try:
            asyncio.run_coroutine_threadsafe(save_data(),bot.loop)
        except Exception as exc:
            pass
    #schedule.every().hour.do(command.get_currencies)
    #schedule.every().day.at("16:30").do(command.get_currencies)

   # while True:
       #schedule.run_pending()
       #time.sleep(1)