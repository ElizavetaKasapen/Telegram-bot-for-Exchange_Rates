from datetime import datetime
class Account_properties:
    #Выбор языка
    def get_language (self): 
        return self.language
    def set_language(self, language): 
        self.language = language 
    #Выбор банка 
    def get_bank(self): 
        return self.bank
    def set_bank(self, bank): 
        self.bank = bank
    #Выбор валют 
    def get_currency(self): 
        return self.currency
    def set_currency(self, currency): 
        self.currency = currency 
    #Выбор времени 
    def get_time(self): 
        return self.time
    def set_time(self, time): 
        self.time = time 