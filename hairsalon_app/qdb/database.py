import os 
import oracledb

from hairsalon_app.users.Users import Users

class Database():
     
    def __init__(self, autocommit=True):
        self.__connection = self.__connect()
        self.__connection.autocommit = autocommit

    #Using kwargs from config_db to establish connection
    def __connect(self):
        if __name__ == '__main__':
            from config_db import host, usr, sn, pw
        else:
            from hairsalon_app.qdb.config_db import host, usr, sn, pw
        return oracledb.connect(user=usr, password=pw, host=host,  service_name=sn) 
    
    #returns connection
    def  db_conn (self): 
        return self.__connection
    
    def close(self):
        '''Closes the connection'''
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None

    def __reconnect(self):
        try:
            self.close()
        except oracledb.Error as f:
            pass
        self.__connection = self.__connect()

    def __run_file(self, file_path):
        statement_parts = []
        with self.__connection.cursor() as cursor:
            # pdb.set_trace()
            with open(file_path, 'r') as f:
                for line in f:
                    if line[:2]=='--': continue
                    statement_parts.append(line)
                    if line.strip('\n').strip('\n\r').strip().endswith(';'):
                        statement = "".join( statement_parts).strip().rstrip(';')
                        if statement:
                            try:
                                # pdb.set_trace()
                                cursor.execute(statement)
                            except Exception as e:
                                print(e)
                        statement_parts = []
    def get_cursor(self):
        for i in range(3):
            try:
                return self.__connection.cursor()
            except Exception as e:
                # Might need to reconnect
                self.__reconnect()

# ---------Work in your code blocks --------!!!!!!!*

# ---------Amy 


# ---------Iana
#Get the list of professionals
    def get_users_professional(self):
        '''Returns all user objects in a list'''
        list_professionals = []
        try:
            with self.get_cursor() as cur:
                qry = f" select * from salon_proffesional"
                r = cur.execute(qry).fetchall()
                for professional in r:
                    list_professionals.append(Users(professional[3]))
        except Exception as e:
            print(e)
        return list_professionals 
    
#Get the list of clients
    def get_users_clients(self):
        '''Returns all user objects in a list'''
        list_clients = []
        try:
            with self.get_cursor() as cur:
                qry = f" select * from salon_client"
                r = cur.execute(qry).fetchall()
                for client in r:
                    list_clients.append(Users(client[3]))
        except Exception as e:
            print(e)
        return list_clients 
#Add a new user
    #Add a new client
    def add_new_client(self,username):
        '''  method to add a new client, data coming fro a user input form'''
        with self.get_cursor() as cur:
            qry = "INSERT INTO salon_client(username)"
            try:
                cur.execute(qry,(username))
                self.__connection.commit()
            except Exception as e:
                print(e)
    #Add a new proffesional
    def add_new_proffesional(self,username):
        '''  method to add a new proffesional, data coming fro a user input form'''
        with self.get_cursor() as cur:
            qry = "INSERT INTO salon_professional(username)"
            try:
                cur.execute(qry,(username))
                self.__connection.commit()
            except Exception as e:
                print(e)
# ----------------------

# ---------Darina





#----------END of work area -----------

# if __name__ != '__main__':
    #import things 

        # ----------------------                   
        # ----------------------------
        #  1.	Create two global variables:
        # •	an instance of Database class that you call db.
database = Database()

# 2.	Call run_sql_script on da1tabase.sql  if the script (database.py) is run in isolation.

if __name__ == '__main__':
    database.run_sql_script('schema.sql')