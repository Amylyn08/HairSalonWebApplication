import os 
import oracledb

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

# ---------Work in your code blocks --------!!!!!!!*

# ---------Amy 


# ---------Iana 


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