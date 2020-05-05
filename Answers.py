import requests
import re
class Answers: 
    privat_url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    all_url='http://resources.finance.ua/ru/public/currency-cash.json'
    def get_url_privat(self):
        self.contents = requests.get(self.privat_url).json() 
        return self.contents
    def get_url_all(self):
        self.contents = requests.get(self.all_url).json() 
        return self.contents
    #Privat
    def privat_USD(self):
        self.content=self.get_url_privat()
        self.usd=self.content[0]['buy']+'uah '+ self.content[0]['sale']+'uah '
        return self.usd
    def privat_EUR(self):
        self.content=self.get_url_privat()
        self.usd=self.content[1]['buy']+'uah '+ self.content[1]['sale']+'uah '
        return self.usd
    def privat_RU(self):
        self.content=self.get_url_privat()
        self.usd=self.content[2]['buy']+'uah '+ self.content[2]['sale']+'uah '
        return self.usd
    #Alfa
    def alfa_USD(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][6]['currencies']['USD']['bid']
        self.sale=self.content['organizations'][6]['currencies']['USD']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd
    def alfa_EUR(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][6]['currencies']['EUR']['bid']
        self.sale=self.content['organizations'][6]['currencies']['EUR']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    def alfa_RU(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][6]['currencies']['RUB']['bid']
        self.sale=self.content['organizations'][6]['currencies']['RUB']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    #Oshad
    def oshad_USD(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][39]['currencies']['USD']['bid']
        self.sale=self.content['organizations'][39]['currencies']['USD']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd
    def oshad_EUR(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][39]['currencies']['EUR']['bid']
        self.sale=self.content['organizations'][39]['currencies']['EUR']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    def oshad_RU(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][39]['currencies']['RUB']['bid']
        self.sale=self.content['organizations'][39]['currencies']['RUB']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
     #Pumb
    def pumb_USD(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][45]['currencies']['USD']['bid']
        self.sale=self.content['organizations'][45]['currencies']['USD']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd
    def pumb_EUR(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][45]['currencies']['EUR']['bid']
        self.sale=self.content['organizations'][45]['currencies']['EUR']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    def pumb_RU(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][45]['currencies']['RUB']['bid']
        self.sale=self.content['organizations'][45]['currencies']['RUB']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    #agrikol
    def agrikol_USD(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][26]['currencies']['USD']['bid']
        self.sale=self.content['organizations'][26]['currencies']['USD']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd
    def agrikol_EUR(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][26]['currencies']['EUR']['bid']
        self.sale=self.content['organizations'][26]['currencies']['EUR']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 
    def agrikol_RU(self):
        self.content=self.get_url_all()
        self.buy=self.content['organizations'][26]['currencies']['RUB']['bid']
        self.sale=self.content['organizations'][26]['currencies']['RUB']['ask']
        self.usd=self.buy+'uah '+ self.sale+'uah '
        return self.usd 