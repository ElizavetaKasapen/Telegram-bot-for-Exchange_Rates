import sqlite3

class DB:
    __connection=None
    def get_connection(self):
        if self.__connection is None:
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
             language TEXT
             )''')
        self.con.commit()
    def add_user(self,user_id:str,banks:str,currencies:str,language:str='ukr',time:str='9:00'):
        self.con=self.get_connection()
        self.c=self.con.cursor()
        self.c.execute('INSERT INTO account_prop(user_id,banks,currencies,language,time)  VALUES(?,?,?,?,?)',(user_id,banks,currencies,language,time))
        self.con.commit()
        