from telegram.ext import Updater, CommandHandler
import requests
import re
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,PollOption
import Account_properties
import Handlers
import Keyboards
from datetime import datetime
import DB
import Str_for_DB
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='bot_activity.log')
srt_db=Str_for_DB.Str_for_DB()
db_=DB.DB()
handler=Handlers.Handlers()
properties=Account_properties.Account_properties()
boards = Keyboards.Keyboards()
class Commands: 
    currencies={'USD':False,'EUR':False,'RUB':False}#список выбранных валют
    banks = {'ПриватБанк':False,'Альфа-Банк':False,'Ощадбанк':False,'ПУМБ':False,'Креді Агріколь':False}
    
    def banks_statistics(self,update, context):
        self.bank=db_.bank_statistics()
        self.out=''
        self.user=''
        if db_.select_language(properties.get_adm())=='ukr':self.user+=" користувачів\n" 
        if db_.select_language(properties.get_adm())=='rus':self.user+=" пользователей\n" 
        for key,value in self.bank.items():
            self.out+=key+": "+str(value)+self.user
        context.bot.send_message(chat_id=update.message.chat_id, text=self.out)
    def start(self,update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text="""Вітаю!\nБудь ласка, перед початком роботи оберіть комфортні для вас налаштування.
Обов'язково оберить валюти і банки!
Після цього надішліть команду /save_information.
Приємного користування!""")
        curr_markup = InlineKeyboardMarkup(boards.currency_board(self.currencies))
        update.message.reply_text('Оберіть валюту/валюти:', reply_markup=curr_markup)
        banks_markup = InlineKeyboardMarkup(boards.banks_board(self.banks))
        update.message.reply_text('Оберіть банк(и):', reply_markup=banks_markup)
        time_markup = InlineKeyboardMarkup(boards.time_board())
        update.message.reply_text('Оберіть час для відправлення повідомлення:', reply_markup=time_markup)
        language_markup = InlineKeyboardMarkup(boards.language_board())
        update.message.reply_text('Оберіть мову:', reply_markup=language_markup)
 
    def save(self,update, context):
        id_ = str(update.message.from_user.id)
        ban=srt_db.srt_for_curr(properties.get_bank())
        cur=srt_db.srt_for_curr(properties.get_currency())
        lang=properties.get_language()
        tim=properties.get_time()
        logging.info("Saving person with "+id_+" ID")
        db_.add_user(id_,ban,cur,lang,tim)
        context.bot.send_message(chat_id=update.message.chat_id, text="Ok!😄")
    def get_currencies(self,update, context):
        txt=''
        banks_=db_.select_banks(update.message.from_user.id)
        currencies_=db_.select_currencies(update.message.from_user.id)
        for b_key, b_value in banks_.items():
            if b_value:
                txt+="\n"+b_key+"\n"
                txt+=handler.choose_output(b_key,currencies_,update.message.from_user.id)
        context.bot.send_message(chat_id=update.message.chat_id, text=txt)
        logging.info(txt)
    def button(self,update, context):
        query = update.callback_query
        if query.data=='ukr'or query.data=='rus': 
            answ = handler.choose_language(query.data)
            properties.set_language(query.data)
            query.edit_message_text(text=answ)
        if query.data=='USD':
            self.currencies['USD']=not self.currencies['USD']
            self.change_buttons_curr(update,self.currencies)
        if query.data=='EUR':
            self.currencies['EUR']=not self.currencies['EUR']
            self.change_buttons_curr(update,self.currencies)
        if query.data=='RUB':
            self.currencies['RUB']=not self.currencies['RUB']
            self.change_buttons_curr(update,self.currencies)
        if query.data=='done_curr':
            answ=handler.choose_currency(self.currencies)
            query.edit_message_text(text=answ)
            properties.set_currency(self.currencies)
        if query.data=='ПриватБанк':
            self.banks['ПриватБанк']=not self.banks['ПриватБанк']
            self.change_buttons_banks(update,self.banks)
        if query.data=='Альфа-Банк':
            self.banks['Альфа-Банк']=not self.banks['Альфа-Банк']
            self.change_buttons_banks(update,self.banks)
        if query.data=='Ощадбанк':
            self.banks['Ощадбанк']=not self.banks['Ощадбанк']
            self.change_buttons_banks(update,self.banks)
        if query.data=='Креді Агріколь':
            self.banks['Креді Агріколь']=not self.banks['Креді Агріколь']
            self.change_buttons_banks(update,self.banks)
        if query.data=='ПУМБ':
            self.banks['ПУМБ']=not self.banks['ПУМБ']
            self.change_buttons_banks(update,self.banks)
        if query.data=='done_banks':
            answ=handler.choose_banks(self.banks)
            properties.set_bank(self.banks)
            query.edit_message_text(text=answ)  
        if query.data=='9:00':
            properties.set_time('9:00')
            query.edit_message_text(text="Повідомлення буде надсилатись щодня о 9:00")  
        if query.data=='15:00':
            properties.set_time('15:00')
            query.edit_message_text(text="Повідомлення буде надсилатись щодня о 15:00")  
        if query.data=='21:00':
            properties.set_time('21:00')
            query.edit_message_text(text="Повідомлення буде надсилатись щодня о 21:00") 

            
    def change_buttons_curr(self,update,curr):
        query = update.callback_query
        curr_markup = InlineKeyboardMarkup(boards.currency_board(curr))
        query.edit_message_text('Оберіть валюту/валюти:', reply_markup=curr_markup)
    def change_buttons_banks(self,update,banks):
        query = update.callback_query
        banks_markup = InlineKeyboardMarkup(boards.banks_board(banks))
        query.edit_message_text('Оберіть банк(и):', reply_markup=banks_markup)
    def help(self,update, context):
        out=''
        id_=update.message.from_user.id
        if db_.select_language(properties.get_adm())=='ukr':
            self.out+="""Вітаю у розділі "допомога"!
Для того, щоб користуватись ботом, Вам необхідно:
1. Пройти стартову реєстрацію (/start), де ОБОВ'ЯЗКОВО вказати банки та валюти про які Ви хочете отримувати інформацію.
   Якщо Ви не оберете час та мову, система зробить це за Вас. За замовчуванням: українська мова та час відправлення о 9:00.
2. Після реєстрації ОБОВ'ЯЗКОВО викличе команду /save_information, щоб система Вас запам'ятала та виводила необхідну Вам інформацію.
Для отримання інформації щодо поточного курсу валют введіть команду /get_currencies.
Щоб відправити повідомлення адміністратору введіть команду /message_to_administrator та в цьому ж повідомленні напишіть своє питання або повідомлення про помилку.
Приємного користування!""" 
            if id_==properties.get_adm():
                self.out+="""Оскільки Ви адміністратор цього боту, для Вас є окремі команди:
/banks_statistics - виведення статистики про кількість користувачів, які обрали доступні банки
/time_statistics - виведення статистики про кількість користувачів, які обрали доступний час для відправлення повідомлень
/currencies_statistics - виведення статистики про кількість користувачів, які обрали доступні курси валют
/message_to_users - відправлення повідомлення всім користувачам (напишіть ваше повідомлення в одному повідомленні з командою)"""
        if db_.select_language(properties.get_adm())=='rus':
            self.out+="""Приветствую в разделе "помощь"!
Чтобы пользоваться ботом, Вам необходимо:
1. Пройти стартовую регистрации (/start), где ОБЯЗАТЕЛЬНО указать банки и валюты о которых Вы хотите получать информацию.
   Если не выбраны время и язык, система сделает это за Вас. По умолчанию: украинский язык и время отправления в 9:00.
2. После регистрации ОБЯЗАТЕЛЬНО вызовете команду /save_information, чтобы система Вас запомнила и выводила необходимую Вам информацию.
Для получения информации о текущем курсе валют введите команду /get_currencies.
Чтобы отправить сообщение администратору введите команду /message_to_administrator и в этом же сообщении напишите свой вопрос или сообщение об ошибке.
Приятного использования! """
        if id_==properties.get_adm():
            self.out+= """Поскольку Вы администратор этого бота, для Вас есть отдельные команды:
/banks_statistics - вывод статистики о количестве пользователей, которые доступны банки
/time_statistics - вывод статистики о количестве пользователей, которые доступное время для отправки сообщений
/currencies_statistics - вывод статистики о количестве пользователей, которые доступны курсы валют
/message_to_users - отправка сообщения всем пользователям (напишите ваше сообщение в одном сообщении с командой) """
        context.bot.send_message(chat_id=update.message.chat_id, text=out)
