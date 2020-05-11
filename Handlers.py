from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import Account_properties
import Answers
import DB
db_=DB.DB()
#import telebot
properties=Account_properties.Account_properties()
answ = Answers.Answers()
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
            if value:txt+=key+"\n"
        return txt
    def choose_output(self,bank,currency,id):
        out=''
        if db_.select_language(id)=='ukr':out+="Купівля             Продаж\n" 
        if db_.select_language(id)=='rus':out+="Купля               Продажа\n" 
        if bank=='ПриватБанк':
            for key, value in currency.items():
                if value and key=='USD': out+='USD\n'+answ.privat_USD()
                if value and key=='EUR': out+='EUR\n'+answ.privat_EUR()
                if value and key=='RUB': out+='RUB\n'+answ.privat_RU()
        if bank=='Альфа-Банк':
            for key, value in currency.items():
                if value and key=='USD': out+='USD\n'+answ.alfa_USD()
                if value and key=='EUR': out+='EUR\n'+answ.alfa_EUR()
                if value and key=='RUB': out+='RUB\n'+answ.alfa_RU()
        if bank=='Ощадбанк':
            for key, value in currency.items():
                if value and key=='USD': out+='USD\n'+answ.oshad_USD()
                if value and key=='EUR': out+='EUR\n'+answ.oshad_EUR()
                if value and key=='RUB': out+='RUB\n'+answ.oshad_RU()       
        if bank=='ПУМБ':
            for key, value in currency.items():
                if value and key=='USD': out+='USD\n'+answ.pumb_USD()
                if value and key=='EUR': out+='EUR\n'+answ.pumb_EUR()
                if value and key=='RUB': out+='RUB\n'+answ.pumb_RU()          
        if bank=='Креді Агріколь':
            for key, value in currency.items():
                if value and key=='USD': out+='USD\n'+answ.agrikol_USD()
                if value and key=='EUR': out+='EUR\n'+answ.agrikol_EUR()
                if value and key=='RUB': out+='RUB\n'+answ.agrikol_RU()
        return out