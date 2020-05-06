from telegram.ext import Updater, CommandHandler,CallbackQueryHandler
import requests
import re
import Commands
from telegram import ReplyKeyboardMarkup
com = Commands.Commands()
updater = Updater('1120461749:AAF_gXcuweGZFpUJ_SdFQesGUxwWcZu0O-M',use_context=True)



def main():
    dp = updater.dispatcher
    help()
    dp.add_handler(CommandHandler('start',com.start))
    dp.add_handler(CommandHandler('get_currencies',com.get_currencies))
    dp.add_handler(CallbackQueryHandler(com.button))
    updater.start_polling()
    updater.idle()
def help():
        contents = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json() 
        usd=contents[0]['buy']+'uah '+ contents[0]['sale']+'uah \n'
        eu=contents[1]['buy']+'uah '+ contents[1]['sale']+'uah \n'
        ru=contents[2]['buy']+'uah '+ contents[2]['sale']+'uah \n'
        a=2+5
if __name__ == '__main__':
    main()