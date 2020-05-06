from telegram.ext import Updater, CommandHandler
import requests
import re
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,PollOption
import Account_properties
import Handlers
import Keyboards
from datetime import datetime
handler=Handlers.Handlers()
properties=Account_properties.Account_properties()
boards = Keyboards.Keyboards()
class Commands: 
    currencies={'USD':False,'EUR':False,'RUB':False}#список выбранных валют
    banks = {'ПриватБанк':False,'Альфа-Банк':False,'Ощадбанк':False,'ПУМБ':False,'Креді Агріколь':False}
 
    def start(self,update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text="Вітаю!\nБудь ласка, перед початком роботи оберіть комфортні для вас налаштування")
        curr_markup = InlineKeyboardMarkup(boards.currency_board(self.currencies))
        update.message.reply_text('Оберіть валюту/валюти:', reply_markup=curr_markup)
        banks_markup = InlineKeyboardMarkup(boards.banks_board(self.banks))
        update.message.reply_text('Оберіть банк(и):', reply_markup=banks_markup)
        time_markup = InlineKeyboardMarkup(boards.time_board())
        update.message.reply_text('Оберіть час для відправлення повідомлення:', reply_markup=time_markup)
        language_markup = InlineKeyboardMarkup(boards.language_board())
        update.message.reply_text('Оберіть мову:', reply_markup=language_markup)
    def get_currencies(self,update, context):
        txt=''
        banks_=properties.get_bank()
        currencies_=properties.get_currency()
        for b_key, b_value in banks_.items():
            if b_value==True:
                txt+="\n"+b_key+"\n"
                txt+=handler.choose_output(b_key,currencies_)
        context.bot.send_message(chat_id=update.message.chat_id, text=txt)
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