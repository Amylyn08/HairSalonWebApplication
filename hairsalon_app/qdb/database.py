from multiprocessing.connection import Client
import os 
import oracledb  
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.users.Member import Member
from hairsalon_app.users.Professional import Profesionnal

#from hairsalon_app.users.Client import Client

#from hairsalon_app.users.Professional import Profesionnal

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
    
    def __reconnect(self):
        try:
            self.close()
        except oracledb.Error as f:
            pass
        self.__connection = self.__connect()

    def run_sql_script(self, sql_filename):
        if os.path.exists(sql_filename):
            self.__connect()
            self.__run_file(sql_filename)
            self.close()
        else:
            print('Invalid Path')

    def get_cursor(self):
        for i in range(3):
            try:
                return self.__connection.cursor()
            except Exception as e:
                # Might need to reconnect
                self.__reconnect()

# ---------Work in your code blocks --------!!!!!!!*

# ---------Amy 

#this function saves the passed in as parameter to the database.
# def save_image_to_db(self, hexed_file_name):
#     try:
#         with self.__connection.cursor() as cursor:
#             qry='''INSERT INTO salon_user (user_image)
#                     VALUES(:hexed_file_name)'''
#         cursor.execute(qry, hexed_file_name=hexed_file_name)
#     except Exception as e:
#         print(f'The following error has occured: {e}')



# ---------Iana
#Get the list of professionals
#     def get_users_professional(self):
#         '''Returns all client objects in a list'''
#         list_professionals = []
#         try:
#             with self.get_cursor() as cur:
#                 qry = f" select * from salon_proffesional"
#                 r = cur.execute(qry).fetchall()
#                 for professional in r:
#                     list_professionals.append(Profesionnal(professional[3],professional[4],professional[5],professional[6],professional[7],professional[8],professional[9],professional[10],professional[11],professional[12]))
#         except Exception as e:
#             print(e)
#         return list_professionals 
    
# #Get the list of clients
#     def get_users_clients(self):
#         '''Returns all profesionnal objects in a list'''
#         list_clients = []
#         try:
#             with self.get_cursor() as cur:
#                 qry = f" select * from salon_client"
#                 r = cur.execute(qry).fetchall()
#                 for client in r:
#                     list_clients.append(Client(client[3],client[4],client[5],client[6],client[7],client[8],client[9],client[10]))
#         except Exception as e:
#             print(e)
#         return list_clients 
#Add a new user
    #Add a new client

    def add_new_client(self,username,full_name, email, user_image,password, phone, address, age):
        '''  method to add a new client, data coming fro a user input form'''
        with self.get_cursor() as cur:
            qry = '''INSERT INTO salon_user(username,full_name, email, user_image,password, phone, address, age)
                        VALUES(:username, :full_name, :email, :user_image, :password, :phone, :address, :age)'''
            try:
                cur.execute(qry, username=username, full_name=full_name, email=email, user_image=user_image,
                                 password=password, phone=phone, address=address, age=age )
                self.__connection.commit()
            except Exception as e:
                print(f'The following error occured: {e}')
    #Add a new proffesional

def add_new_pro(self, username, full_name, email, user_image, password, phone, address, age, speciality, payrate):
    ''' Method to add a new professional, data coming from a user input form '''
    with self.get_cursor() as cur:
        qry = '''INSERT INTO salon_professional(user_type, username, full_name, email,
                                                user_image, password_hashed,
                                                phone_number, address, age, specialty, pay_rate)
                VALUES ('professional', :username, :full_name, :email, :user_image, :password,
                        :phone, :address, :age, :specialty, :payrate)'''
        try:
            cur.execute(qry, {'username': username, 'full_name': full_name, 'email': email, 'user_image': user_image,
                              'password': password, 'phone': phone, 'address': address, 'age': age,
                              'specialty': speciality, 'payrate': payrate})
            self.__connection.commit()
        except Exception as e:
            print(e)


# def get_client(self, username):
#     try:
#         with self.__connection.cursor() as cursor:
#             qry ='''SELECT username,
#                             full_name, 
#                             email, 
#                             user_image, 
#                             password_hashed, 
#                             phone_number
#                             address,
#                             age 
#                     WHERE username=:username
#                             '''
#             cursor.execute(qry, username=username)
#             rows = cursor.fetchall()
#             client_list = []
#             for client in rows:
#                 client_list.append(Client(*client))
#             return client_list
#     except Exception as e:
#         print(f'The following error occured: {e}')

def get_member(self, username):
    try:
        with self.__connection.cursor() as cursor:
            qry ='''SELECT  user_type,
                            username,
                            full_name, 
                            email, 
                            user_image, 
                            password_hashed, 
                            phone_number
                            address,
                            age,
                            specialty,
                            pay_rate
                    WHERE username=:username
                            '''
            cursor.execute(qry, username=username)
            rows = cursor.fetchall()
            member_list = []
            for member in rows:
                member_list.append(Member(*member))
            return member_list
    except Exception as e:
        print(f'The following error occured: {e}')
    
    #Selects client based on the username                
    # def get_client_user(self, username):
    #     oneclient= []
    #     with self.get_cursor() as cur:
    #         qry = f"SELECT * FROM salon_client WHERE username='{username}'"
    #         try:
    #             clients = cur.execute(qry).fetchall()
    #             for client in clients:
    #                 oneclient.append(Client(client[3],client[4],client[5],client[6],client[7],client[8],client[9],client[10]))
    #         except Exception as e:
    #             print(e)
    #     return oneclient
# ----------------------

# ---------Darina

    # def get_my_appointments(self, client_id):
    #     ''' method to list all appointments of a given client '''
    #     appointments = []
    #     try:
    #         with self.__connection.cursor() as c:
    #             sql = f'SELECT * FROM salon_appointment WHERE client_id= :client_id'
    #             info = {'client_id':client_id}
    #             fetch = c.execute(sql, info).fetchall()
    #             appointments.append(Appointment((fetch[0], fetch[1], fetch[2],fetch[3], fetch[4], fetch[5], fetch[6])))
    #     except Exception as e:
    #         print(e)
        
    #     return appointments
    
    # def get_all_appointments(self):
    #     ''' method to list all appointments '''
    #     appointments = []
    #     try:
    #         with self.__connection.cursor() as c:
    #             sql = f'SELECT * FROM salon_appointment'
    #             fetch = c.execute(sql).fetchall()
    #             appointments.append(Appointment((fetch[0], fetch[1], fetch[2],fetch[3], fetch[4], fetch[5], fetch[6])))
    #     except Exception as e:
    #         print(e)
        
    #     return appointments

# add new address to database
    def add_new_appointment(self, appointment_id, status, approved, date_appointment, client_id, professional_id, service_id):
        '''  method to schedule a new appointment, data coming fro a user input form'''
        try:
            with self.__connection.cursor() as cursor:
                sql = f'INSERT INTO salon_appointment (appointment_id, status, approved, date_appointment, client_id, professional_id, service_id) VALUES ( :appointment_id, :status, :approved, :date_appointment, :client_id, :professional_id, :service_id)'
                info = {'appointment_id' : appointment_id, 'status': status, 'approved': approved, 'date_appointment': date_appointment, 'client_id' : client_id, 'professional_id': professional_id, 'service_id': service_id}
                cursor.execute(sql, info)
                self.__connection.commit()
        except Exception as e:
            print (e)






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
    database.run_sql_script('schemasql')