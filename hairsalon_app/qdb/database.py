from multiprocessing.connection import Client
import os 
import oracledb  
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.users.Member import Member
from hairsalon_app.report_view.report import Report
import pdb



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
# Get the list of user
    def get_users(self):
        '''Returns all users objects in a list'''
        list_users = []
        try:
            with self.get_cursor() as cur:
                qry = f" select * from salon_user"
                users = cur.execute(qry).fetchall()
                for user in users:
                    list_users.append(Member(user[2],user[3],user[4],user[5],user[6],user[7],user[8],user[9],user[10],user[11],user[12],user[13]))
        except Exception as e:
            print(e)
        return list_users 
    
#Add a new user
    #Add a new client

    def add_new_client(self,username,full_name, email, user_image,password, phone, address, age):
        '''  method to add a new client, data coming fro a user input form'''
        try:
            with self.__connection.cursor() as cur:
                qry = '''INSERT INTO salon_user(username,full_name, email, user_image,password_hashed, phone_number, address, age)
                            VALUES(:username, :full_name, :email, :user_image, :password, :phone, :address, :age)'''
                
                cur.execute(qry, username=username, full_name=full_name, email=email, user_image=user_image,
                                    password=password, phone=phone, address=address, age=age )
        except Exception as e:
                print(f'The following error occured: {e}')
    #Add a new proffesional

    def add_new_pro(self, username, full_name, email, user_image, password, phone, address, age, speciality, payrate):
        ''' Method to add a new professional, data coming from a user input form '''
        with self.get_cursor() as cur:
            qry = '''INSERT INTO salon_user(user_type, username, full_name, email,
                                                    user_image, password_hashed,
                                                    phone_number, address, age, specialty, pay_rate)
                    VALUES ('professional', :username, :full_name, :email, :user_image, :password,
                            :phone, :address, :age, :specialty, :payrate)'''
            try:
                cur.execute(qry, {'username': username, 'full_name': full_name, 'email': email, 'user_image': user_image,
                                'password': password, 'phone': phone, 'address': address, 'age': age,
                                'specialty': speciality, 'payrate': payrate})
            except Exception as e:
                print(e)

    def get_list_pros(self):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT user_id,
                                is_active,
                                user_type,
                                status,
                                username,
                                full_name, 
                                email, 
                                user_image, 
                                password_hashed, 
                                phone_number,
                                address,
                                age,
                                specialty,
                                pay_rate
                        FROM salon_user
                        WHERE user_type='professional' '''
                cursor.execute(qry)
                rows = cursor.fetchall()
                pros_list = []
                for pro in rows:
                    pros_list.append(Member(*pro))
                return pros_list
        except Exception as e:
            print(f'Error retrieving member: {e}')

    def get_all_users(self):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT user_id,
                                is_active,
                                user_type,
                                status,
                                username,
                                full_name, 
                                email, 
                                user_image, 
                                password_hashed, 
                                phone_number,
                                address,
                                age,
                                pay_rate, 
                                specialty
                        FROM salon_user
                         WHERE user_type NOT IN ('admin_super', 'client') '''
                cursor.execute(qry)
                rows = cursor.fetchall()
                users_list = []
                for user in rows:
                    users_list.append(Member(*user))
                return users_list
        except Exception as e:
            print(f'Error retrieving member: {e}')

    def get_list_clients(self):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT user_id,
                                is_active,
                                user_type,
                                status,
                                username,
                                full_name, 
                                email, 
                                user_image, 
                                password_hashed, 
                                phone_number,
                                address,
                                age,
                                pay_rate, 
                                specialty
                        FROM salon_user
                        WHERE user_type='client' '''
                cursor.execute(qry)
                rows = cursor.fetchall()
                clients_list = []
                for client in rows:
                    clients_list.append(Member(*client))
                return clients_list
        except Exception as e:
            print(f'Error retrieving member: {e}')

    def get_all_admin_username(self):
        try:
            with self.__connection.cursor() as c:
                qry='''SELECT username FROM SALON_USER WHERE user_type LIKE 'admin%' '''
                c.execute(qry)
                names = c.fetchall()
                return names
        except Exception as e:
            print(f'Error retrieving member: {e}')

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

    # Iana code
    def update_profile(self,username, new_password, full_name, email, phone_number, address, user_image):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''UPDATE salon_user
                        SET password_hashed = :new_password,
                            full_name = :full_name,
                            email = :email,
                            phone_number = :phone_number,
                            address = :address,
                            user_image = :user_image
                        WHERE username = :username'''
                cursor.execute(qry,username=username,new_password=new_password,full_name=full_name,email=email,phone_number=phone_number,address=address,user_image=user_image)
                self.__connection.commit()
        except Exception as e:
            print(f'Error updating member: {e}')
    
    # def update_image(self,username, user_image):
    #     try:
    #         with self.__connection.cursor() as cursor:
    #             qry = '''UPDATE salon_user
    #                     SET user_image = :user_image
    #                         WHERE username = :username'''
    #             cursor.execute(qry,username=username,user_image=user_image)
    #             self.__connection.commit()
    #     except Exception as e:
    #         print(f'Error updating member: {e}')
    

    
    def get_member(self, username):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT user_id,
                                is_active,
                                user_type,
                                status,
                                username,
                                full_name, 
                                email, 
                                user_image, 
                                password_hashed, 
                                phone_number,
                                address,
                                age,
                                specialty,
                                pay_rate
                        FROM salon_user
                        WHERE username = :username'''
                cursor.execute(qry, username=username)
                row = cursor.fetchone()
                if row:
                    member = Member(*row)
                    return member
                else:
                    return None
        except Exception as e:
            print(f'Error retrieving member: {e}')
            return None
    
    def get_active(self, username):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT is_active FROM salon_user WHERE username = :username'''
                cursor.execute(qry, username=username)
                row = cursor.fetchone()
                if row:
                    active = row[0]
                    return active
        except Exception as e:
            print(f'Error retrieving member: {e}')

    def set_active(self, username, active):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''UPDATE salon_user SET is_active=:active WHERE username = :username'''
                cursor.execute(qry, username=username, active=active)
        except Exception as e:
            print(f'Error updating member: {e}')
    
    def get_flag(self, username):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''SELECT status FROM salon_user WHERE username = :username'''
                cursor.execute(qry, username=username)
                row = cursor.fetchone()
                if row:
                    flag = row[0]
                    return flag
                else:
                    return None
        except Exception as e:
            print(f'Error retrieving member: {e}')
            
    def set_flag(self, username, status):
        try:
            with self.__connection.cursor() as cursor:
                qry = '''UPDATE salon_user SET status=:status WHERE username = :username'''
                cursor.execute(qry, username=username, status=status)
        except Exception as e:
            print(f'Error updating member: {e}')
    
    
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

    def get_my_appointments(self, user_id):
        ''' method to list all appointments of a given client '''
        appointments = []
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_appointment WHERE client_id = :user_id OR professional_id = :user_id'
                info = {'user_id': user_id}
                c.execute(sql, info)
                rows = c.fetchall()
                appointments = []
                for app in rows:
                    appointments.append(Appointment(*app))
            return appointments
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
                for record in fetch:
                    appointments.append(Appointment(record[0], record[1], record[2],record[3], record[4], record[5], record[6], record[7], record[8]))
        except Exception as e:
            print(e)
        
        return appointments
        
    def get_appointment_by_client_date(self, username, date):
        try:
            with self.__connection.cursor() as c:
                qry = '''
                    SELECT
                        appointment_id
                    FROM
                        salon_appointment
                    INNER JOIN
                        salon_user ON salon_appointment.client_id = salon_user.user_id
                    WHERE
                        date_appointment = :date
                        AND salon_user.username = :username
                '''
                c.execute(qry, {"date": date, "username": username})
                appointments = c.fetchall()
                # Process appointments as needed
                return appointments
        except Exception as e:
            # Handle exceptions
            print(e)


# add new appointment to database
    def add_new_appointment(self, username, professional, service, venue, slot, date):
        '''  method to schedule a new appointment, data coming fro a user input form'''
        try:
            with self.__connection.cursor() as cursor:
                sql = f'''INSERT INTO salon_appointment (client_id, professional_id, service_id, slot, venue, date_appointment) 
                            VALUES ((SELECT user_id FROM salon_user WHERE username = :username), 
                                    (SELECT user_id FROM salon_user WHERE username = :professional), 
                                    (SELECT service_id FROM salon_service WHERE service_name = :service), 
                                    :slot, :venue, :date_appointment)'''
                info = {'username' : username, 'professional': professional, 'service': service, 'slot': slot, 'venue': venue, 'date_appointment': date}
                cursor.execute(sql, info)
                self.__connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

# add new report to database
    def add_new_report(self,user_id, appointment_id, title, client_report, professional_report):
        '''  method to schedule a new appointment, data coming fro a user input form'''
        try:
            with self.__connection.cursor() as cursor:
                sql = f'''INSERT INTO salon_report (user_id, appointment_id, title, client_report, professional_report) 
                            VALUES (:user_id,
                                    :appointment_id, 
                                    :title, 
                                    :client_report, 
                                    :professional_report)'''
                info = {'user_id': user_id,'appointment_id' : appointment_id, 'title': title, 'client_report': client_report, 'professional_report': professional_report}
                cursor.execute(sql, info)
                self.__connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')
            
    def edit_report(self, report_id, new_client_report, new_professional_report):
        '''  method to edit existing report in database'''
        try:
            with self.__connection.cursor() as cursor:
                sql = f'''UPDATE salon_report
                            SET client_report = :client_report, professional_report = :professional_report
                            WHERE report_id = :report_id'''
                info = {'report_id' : report_id, 'client_report': new_client_report, 'professional_report': new_professional_report}
                cursor.execute(sql, info)
                self.__connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

    def get_all_reports(self):
        ''' method to list all reports '''
        reports = []
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_report'
                fetch = c.execute(sql).fetchall()
                print(len(fetch))
                for record in fetch:
                    print(record)
                    reports.append(Report(record[0], record[1], record[2],record[3], record[4], record[5], record[6]))
        except Exception as e:
            print(e)
        
        return reports
    
    def get_appointment_reports(self, appointment_id):
        ''' method to list all reports of a specific appointment'''
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_report WHERE appointment_id = :appointment_id'
                info = {'appointment_id' : appointment_id}
                c.execute(sql, info)
                rows = c.fetchall()
                reports = []
                for report in rows:
                    reports.append(Report(*report))
            return reports      
        except Exception as e:
            print(f'The following exception occured: {e}')
        
    def get_report_by_id(self, report_id):
        ''' method to retrieve report by its id'''
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_report WHERE report_id = :report_id'
                info = {'report_id' : report_id}
                c.execute(sql, info)
                row = c.fetchone()
                if row:
                    report = Report(*row)
                    return report
                else:
                    return None
        except Exception as e:
            print(f"The followning exception occured: {e}")
                

    def get_all_services(self):
        service_names = []
        try:
            with self.__connection.cursor() as c:
                qry = '''
                    SELECT
                        service_name
                    FROM
                        salon_service
                '''
                c.execute()
                services = c.fetchall()
                for service in services:
                    service_names.append(service)

                # Process appointments as needed
                return services
        except Exception as e:
            # Handle exceptions
            print(e)
    def get_appointment(self, appointment_id):
        try:
            with self.__connection.cursor() as c:
                sql = f'SELECT * FROM salon_appointment WHERE appointment_id = :appointment_id'
                info = {'appointment_id': appointment_id}
                fetch = c.execute(sql, info).fetchone()
                return Appointment(fetch[0], fetch[1], fetch[2],fetch[3], fetch[4], fetch[5], fetch[6], fetch[7], fetch[8])
        except Exception as e:
            print(e)




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
    database.update_image("liliana2020", "michel.png")