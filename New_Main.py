from telegram.ext import Updater, CommandHandler,CallbackQueryHandler
import requests
import re
import Commands
from telegram import ReplyKeyboardMarkup
import DB
import Account_properties
import sqlite3
currencies={'USD':False,'EUR':False,'RUB':False}#список выбранных валют
db_=DB.DB()
#import Time
#time_=Time.Time()
com = Commands.Commands()
updater = Updater('1120461749:AAF_gXcuweGZFpUJ_SdFQesGUxwWcZu0O-M',use_context=True)
properties=Account_properties.Account_properties()
#global __connection    
#__connection=None  
def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',com.start))
    dp.add_handler(CommandHandler('get_currencies',com.get_currencies))
    dp.add_handler(CallbackQueryHandler(com.button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    db_.init_db()
    main()
    