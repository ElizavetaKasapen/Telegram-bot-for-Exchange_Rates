from telegram.ext import Updater, CommandHandler,CallbackQueryHandler
import requests
import re
import Commands
from telegram import ReplyKeyboardMarkup
import DB
import Account_properties
import sqlite3
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='bot_activity.log')
global admin_id 
admin_id ='344587463'
db_=DB.DB()
#import Time
#time_=Time.Time()
com = Commands.Commands()
updater = Updater('1120461749:AAF_gXcuweGZFpUJ_SdFQesGUxwWcZu0O-M',use_context=True)
properties=Account_properties.Account_properties()
#global __connection    
#__connection=None  
import Str_for_DB
srt_db=Str_for_DB.Str_for_DB()

##########################################
def get_connection():
        #if self.__connection is None:
        __connection=sqlite3.connect('properties.db')
        return __connection

def msg_to_adm(update, context):
        username=update.message.from_user.username
        id_=update.message.from_user.id
        out=''
        if username==None: out+='\nUser id:'+str(id_)
        else:out+='\nUser name: @'+str(username)
        text = update.message.text  #ПОЛУЧИТЬ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ
        context.bot.send_message(chat_id=properties.get_adm(), text=text+out)
        logging.info('Msg to adm:'+text+out)
def get_user_id(update):                                                        #НЕ РАБОТАЕТ 
        id_=update.message.from_user.id
        return id_
##########################################

def banks_statistics(update, context):
        bank=db_.bank_statistics()
        out=''
        user=''
        if db_.select_language(properties.get_adm())=='ukr':user+=" користувачів\n" 
        if db_.select_language(properties.get_adm())=='rus':user+=" пользователей\n" 
        for key,value in bank.items():
            out+=key+": "+str(value)+user
        context.bot.send_message(chat_id=update.message.chat_id, text=out)
        logging.info('banks statistics:'+out)
def time_statistics(update, context):
        bank=db_.time_statistics()
        out=''
        user=''
        if db_.select_language(properties.get_adm())=='ukr':user+=" користувачів\n" 
        if db_.select_language(properties.get_adm())=='rus':user+=" пользователей\n" 
        for key,value in bank.items():
            out+=key+": "+str(value)+user
        context.bot.send_message(chat_id=update.message.chat_id, text=out)
        logging.info('time statistics:'+out)
def currencies_statistics(update, context):
        bank=db_.currencies_statistics()
        out=''
        user=''
        if db_.select_language(properties.get_adm())=='ukr':user+=" користувачів\n" 
        if db_.select_language(properties.get_adm())=='rus':user+=" пользователей\n" 
        for key,value in bank.items():
            out+=key+": "+str(value)+user
        context.bot.send_message(chat_id=update.message.chat_id, text=out)  
        logging.info('currencies statistics:'+out)     
def help(update, context):
    out=''
    id_=update.message.from_user.id
    if db_.select_language(properties.get_adm())=='ukr':
            out+="""Вітаю у розділі "допомога"!
Для того, щоб користуватись ботом, Вам необхідно:
1. Пройти стартову реєстрацію (/start), де ОБОВ'ЯЗКОВО вказати банки та валюти про які Ви хочете отримувати інформацію.
   Якщо Ви не оберете час та мову, система зробить це за Вас. За замовчуванням: українська мова та час відправлення о 9:00.
2. Після реєстрації ОБОВ'ЯЗКОВО викличе команду /save_information, щоб система Вас запам'ятала та виводила необхідну Вам інформацію.
Для отримання інформації щодо поточного курсу валют введіть команду /get_currencies.
Щоб відправити повідомлення адміністратору введіть команду /message_to_administrator та в цьому ж повідомленні напишіть своє питання або повідомлення про помилку.
\n""" 
            if str(id_)==properties.get_adm():
                out+="""Оскільки Ви адміністратор цього боту, для Вас є окремі команди:
/banks_statistics - виведення статистики про кількість користувачів, які обрали доступні банки
/time_statistics - виведення статистики про кількість користувачів, які обрали доступний час для відправлення повідомлень
/currencies_statistics - виведення статистики про кількість користувачів, які обрали доступні курси валют
/message_to_users - відправлення повідомлення всім користувачам (напишіть ваше повідомлення в одному повідомленні з командою)"""
    if db_.select_language(properties.get_adm())=='rus':
        out+="""Приветствую в разделе "помощь"!
Чтобы пользоваться ботом, Вам необходимо:
1. Пройти стартовую регистрацию (/start), где ОБЯЗАТЕЛЬНО указать банки и валюты о которых Вы хотите получать информацию.
   Если не выбраны время и язык, система сделает это за Вас. По умолчанию: украинский язык и время отправления в 9:00.
2. После регистрации ОБЯЗАТЕЛЬНО вызовете команду /save_information, чтобы система Вас запомнила и выводила необходимую Вам информацию.
Для получения информации о текущем курсе валют введите команду /get_currencies.
Чтобы отправить сообщение администратору введите команду /message_to_administrator и в этом же сообщении напишите свой вопрос или сообщение об ошибке.
\n"""
        if str(id_)==properties.get_adm():
            out+= """Поскольку Вы администратор этого бота, для Вас есть отдельные команды:
/banks_statistics - вывод статистики о количестве пользователей, которые выбрали доступные банки
/time_statistics - вывод статистики о количестве пользователей, которые выбрали доступное время для отправки сообщений
/currencies_statistics - вывод статистики о количестве пользователей, которые выбрали доступные курсы валют
/message_to_users - отправка сообщения всем пользователям (напишите Ваше сообщение в одном сообщении с командой) """
    context.bot.send_message(chat_id=update.message.chat_id, text=out)
def message_to_users(update, context):
    users=db_.select_all_users_id()
    text = update.message.text  #ПОЛУЧИТЬ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ
    txt=text.split(' ', maxsplit=1)
    for val in users:
        itm=val[0]
        context.bot.send_message(chat_id=itm, text=txt[1])
    logging.info('Msg to users:'+txt[1])
def main():
    logging.info('Start bot')
    properties.set_adm(admin_id)
    db_.select()
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',com.start))
    dp.add_handler(CommandHandler('save_information',com.save))
    dp.add_handler(CommandHandler('get_currencies',com.get_currencies))
    dp.add_handler(CommandHandler('message_to_administrator',msg_to_adm))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('id',get_user_id))
    #if get_user_id(dp)==properties.get_adm():
    dp.add_handler(CommandHandler('banks_statistics',banks_statistics))
    dp.add_handler(CommandHandler('time_statistics',time_statistics))
    dp.add_handler(CommandHandler('currencies_statistics',currencies_statistics))
    dp.add_handler(CommandHandler('message_to_users',message_to_users))
    dp.add_handler(CallbackQueryHandler(com.button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    db_.init_db()
    main()

