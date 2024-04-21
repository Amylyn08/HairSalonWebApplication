import os 
import oracledb
from hairsalon_app.appointment_view.appointment import Appointment

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

    def get_my_appointments(self, client_id):
        ''' method to list all appointments of a given client '''
        appointments = []
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_appointment WHERE client_id= :client_id'
                info = {'client_id':client_id}
                fetch = c.execute(sql, info).fetchall()
                appointments.append(Appointment((fetch[0], fetch[1], fetch[2],fetch[3], fetch[4], fetch[5], fetch[6])))
        except Exception as e:
            print(e)
        
        return appointments
    
    def get_all_appointments(self):
        ''' method to list all appointments '''
        appointments = []
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_appointment'
                fetch = c.execute(sql).fetchall()
                appointments.append(Appointment((fetch[0], fetch[1], fetch[2],fetch[3], fetch[4], fetch[5], fetch[6])))
        except Exception as e:
            print(e)
        
        return appointments






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