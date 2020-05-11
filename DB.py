import sqlite3

class DB:
    currencies={'USD':False,'EUR':False,'RUB':False}#список выбранных валют
    banks = {'ПриватБанк':False,'Альфа-Банк':False,'Ощадбанк':False,'ПУМБ':False,'Креді Агріколь':False}
    __connection=None
    def get_connection(self):
        #if self.__connection is None:
        self.__connection=sqlite3.connect('properties.db')
        return self.__connection
    def init_db(self,force:bool=False):
        self.con=self.get_connection()
        self.c=self.con.cursor()
        #user info
        if force:
            self.c.execute('DROP TABLE IF EXISTS account_prop')
        self.c.execute('''CREATE TABLE IF NOT EXISTS account_prop(
             id INTEGER PRIMARY KEY,
             user_id TEXT NOT NULL,
             banks TEXT NOT NULL,
             currencies TEXT NOT NULL,
             language_ TEXT,
             time_ TEXT
             )''')
        self.con.commit()
    def add_user(self,user_id:str,banks:str,currencies:str,language:str='ukr',time:str='9:00'):
        con=self.get_connection()
        c= con.cursor()
        if(not  self.if_this_user_exist(user_id)):
            c.execute('INSERT INTO account_prop(user_id,banks,currencies,language_,time_) VALUES(?,?,?,?,?);',(user_id,banks,currencies,language,time))
        else:
            c.execute("""Update account_prop set banks = ?,currencies=?,language_=?,time_=? where user_id = ?;""",(banks,currencies,language,time,user_id))
        con.commit()
    def select_language(self,user_id):
          con=  self.get_connection()
          c=  con.cursor()
          c.execute('select language_ from account_prop where user_id=?;',(user_id,))
          results =   c.fetchall()
          con.commit()  
          return results[0][0]
    def select_time(self,user_id):
          con=  self.get_connection()
          c=  con.cursor()
          c.execute('select time_ from account_prop where user_id=?;',(user_id,))
          results =   c.fetchall()
          con.commit()  
          return results[0][0]
    def select_banks(self,user_id):
          self.con=  self.get_connection()
          self.c=  self.con.cursor()
          self.c.execute('select banks from account_prop where user_id=?;',(user_id,))
          self.results =   self.c.fetchall()
          self.curr=  self.convert_banks(self.results[0][0])
          self.con.commit()  
          return self.curr
    def select_currencies(self,user_id):
          con=  self.get_connection()
          c=  con.cursor()
          c.execute('select currencies from account_prop where user_id=?;',(user_id,))
          results =   c.fetchall()
          curr= self.convert_currencies(results[0][0])
          con.commit()  
          return curr
    def convert_banks(self,res):
        for b_key, b_value in   self.banks.items():
            if b_key in res:self.banks[b_key]=True
            else: self.banks[b_key]=False
        return   self.banks
    def convert_currencies(self,res):
        for b_key, b_value in   self.currencies.items():
            if b_key in res:
               self.currencies[b_key]=True
            else: self.currencies[b_key]=False
        return   self.currencies
    def select(self):
        self.con=self.get_connection()
        self.c=self.con.cursor()
        self.c.execute('select * from account_prop;')
        results = self.c.fetchall()
        self.con.commit()
    # true if exsist
    def if_this_user_exist(self,user_id:str):
        self.con=self.get_connection()
        self.c=self.con.cursor()
        self.c.execute('SELECT * FROM account_prop WHERE user_id = ?;',(user_id,))
        results = self.c.fetchall()
        if(len(results)==0):res= False
        else:res= True
        self.con.commit()
        return res

    def bank_statistics(self):
          bank_statistics= {'ПриватБанк':0,'Альфа-Банк':0,'Ощадбанк':0,'ПУМБ':0,'Креді Агріколь':0}
          self.con=  self.get_connection()
          self.c=  self.con.cursor()
          self.c.execute("select * from account_prop ;")
          res=self.c.fetchall()
          for key,value in bank_statistics.items():
            like='%'+key+'%'
            self.c.execute("select count(*) from account_prop where banks like ?;",(like,))
            res=self.c.fetchall()
            bank_statistics[key] =  res[0][0]
          self.con.commit()  
          return bank_statistics

    def time_statistics(self):
          bank_statistics= {'9:00':0,'15:00':0,'21:00':0}
          self.con=  self.get_connection()
          self.c=  self.con.cursor()
          self.c.execute("select * from account_prop ;")
          res=self.c.fetchall()
          for key,value in bank_statistics.items():
            like='%'+key+'%'
            self.c.execute("select count(*) from account_prop where time_ like ?;",(like,))
            res=self.c.fetchall()
            bank_statistics[key] =  res[0][0]
          self.con.commit()  
          return bank_statistics
    def currencies_statistics(self):
          currencies_statistics={'USD':0,'EUR':0,'RUB':0}
          self.con=  self.get_connection()
          self.c=  self.con.cursor()
          self.c.execute("select * from account_prop ;")
          res=self.c.fetchall()
          for key,value in currencies_statistics.items():
            like='%'+key+'%'
            self.c.execute("select count(*) from account_prop where currencies like ?;",(like,))
            res=self.c.fetchall()
            currencies_statistics[key] =  res[0][0]
          self.con.commit()  
          return currencies_statistics
    def select_all_users_id(self):
        self.con=  self.get_connection()
        self.c=  self.con.cursor()
        self.c.execute("select user_id from account_prop ;")
        res=self.c.fetchall()
        self.con.commit()  
        return res

