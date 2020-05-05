from telegram.ext import Updater, CommandHandler
import requests
import re
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,PollOption
from datetime import datetime
class Keyboards: 
    banks = ['privat','alfa','oshad','pumb','agrikol']
    def language_board(self):
        self.keyboard = [[InlineKeyboardButton("Українська", callback_data='ukr'),
                 InlineKeyboardButton("Російська", callback_data='rus')]]
        return self.keyboard
    def currency_board(self,curr):
        txt1="USD" if  not curr["USD"] else "USD✔"
        txt2="EUR" if  not curr["EUR"] else "EUR✔"
        txt3="RUB" if not curr["RUB"] else "RUB✔"
        self.keyboard = [[InlineKeyboardButton(txt1, callback_data='USD'),
                 InlineKeyboardButton(txt2, callback_data='EUR'),
                 InlineKeyboardButton(txt3, callback_data='RUB')],[InlineKeyboardButton('✔', callback_data='done_curr')]]
        return self.keyboard
    def banks_board(self,banks):
        txt0="ПриватБанк✔" if  banks["ПриватБанк"] else "ПриватБанк"
        txt1="Альфа-Банк✔" if  banks["Альфа-Банк"] else "Альфа-Банк"
        txt2="Ощадбанк✔" if  banks["Ощадбанк"] else "Ощадбанк"
        txt3="ПУМБ✔" if  banks["ПУМБ"] else "ПУМБ"
        txt4="Креді Агріколь✔" if  banks["Креді Агріколь"] else "Креді Агріколь"

        self.keyboard = [[InlineKeyboardButton(txt0, callback_data='ПриватБанк')],
                 [InlineKeyboardButton(txt1, callback_data='Альфа-Банк')],
                 [InlineKeyboardButton(txt2, callback_data='Ощадбанк')],
                 [InlineKeyboardButton(txt3, callback_data='ПУМБ')],
                 [InlineKeyboardButton(txt4, callback_data='Креді Агріколь')],
                 [InlineKeyboardButton('✔', callback_data='done_banks')]]
        return self.keyboard
    def time_board(self):
        self.keyboard = [[InlineKeyboardButton('9:00', callback_data='9:00')],
                 [InlineKeyboardButton('15:00', callback_data='15:00')],
                 [InlineKeyboardButton('21:00', callback_data='21:00')]]
        return self.keyboard
   