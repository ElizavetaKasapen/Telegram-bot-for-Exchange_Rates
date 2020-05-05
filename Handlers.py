from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import Account_properties
#import telebot
properties=Account_properties.Account_properties()
class Handlers: 
    def choose_language(self,choose_language):
        if choose_language=='ukr': 
            properties.set_language('ukr')
            return "Ви обрали українську мову"
        if choose_language=='rus': 
            properties.set_language('rus')
            return "Вы выбрали русский язык"
    def choose_currency(self,choose_currency):
        txt='Ви обрали такі валюти:\n'
        for key, value in choose_currency.items():
            if value==True:txt+=key+"\n"
        return txt
    def choose_banks(self,choose_banks):
        txt='Ви обрали такі банки:\n'
        for key, value in choose_banks.items():
            if value==True:txt+=key+"\n"
        return txt
        