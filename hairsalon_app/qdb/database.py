from multiprocessing.connection import Client
import os
import oracledb  
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.users.Member import Member
from hairsalon_app.report_view.report import Report

class Database():
    #Using kwargs from config_db to establish connection
    def __connect(self, autocommit=True):
        if __name__ == '__main__':
            from config_db import host, usr, sn, pw
        else:
          from hairsalon_app.qdb.config_db import host, usr, sn, pw
        return oracledb.connect(user=usr, password=pw, host=host,  service_name=sn) 
    
    
    def close(self):
        '''Closes the connection'''
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None


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

    def run_sql_script(self, sql_filename):
        if os.path.exists(sql_filename):
            self.__connect()
            self.__run_file(sql_filename)
            self.close()
        else:
            print('Invalid Path')


    def add_new_client(self,username,full_name, email, user_image,password, phone, address, age):
        '''  method to add a new client, data coming fro a user input form'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cur:
                    qry = '''INSERT INTO salon_user(username,full_name, email, user_image,password_hashed, phone_number, address, age)
                                VALUES(:username, :full_name, :email, :user_image, :password, :phone, :address, :age)'''
                    
                    cur.execute(qry, username=username, full_name=full_name, email=email, user_image=user_image,
                                        password=password, phone=phone, address=address, age=age )
                    connection.commit()
        except Exception as e:
                print(f'The following error occured: {e}')
    #Add a new proffesional

    def add_new_pro(self, username, full_name, email, user_image, password, phone, address, age, speciality, payrate):
        ''' Method to add a new professional, data coming from a user input form '''
        with self.__connect() as connection:
            with connection.cursor() as cur:
                qry = '''INSERT INTO salon_user(user_type, username, full_name, email,
                                                        user_image, password_hashed,
                                                        phone_number, address, age, specialty, pay_rate)
                        VALUES ('professional', :username, :full_name, :email, :user_image, :password,
                                :phone, :address, :age, :specialty, :payrate)'''
                try:
                    cur.execute(qry, {'username': username, 'full_name': full_name, 'email': email, 'user_image': user_image,
                                    'password': password, 'phone': phone, 'address': address, 'age': age,
                                    'specialty': speciality, 'payrate': payrate})
                    connection.commit()
                except Exception as e:
                    print(e)
    def add_new_admin_appointment(self, username, full_name, email, user_image, password, phone, address, age, speciality, payrate):
        with self.__connect() as connection:
            with connection.cursor() as cur:
                qry = '''INSERT INTO salon_user(user_type, username, full_name, email,
                                                        user_image, password_hashed,
                                                        phone_number, address, age, specialty, pay_rate)
                        VALUES ('admin_appoint', :username, :full_name, :email, :user_image, :password,
                                :phone, :address, :age, :specialty, :payrate)'''
                try:
                    cur.execute(qry, {'username': username, 'full_name': full_name, 'email': email, 'user_image': user_image,
                                    'password':  password, 'phone': phone, 'address': address, 'age': age,
                                    'specialty': speciality, 'payrate': payrate})
                    connection.commit()
                except Exception as e:
                    print(e)
    def add_new_admin_user(self, username, full_name, email, user_image, password, phone, address, age, speciality, payrate):
        with self.__connect() as connection:
            with connection.cursor() as cur:
                qry = '''INSERT INTO salon_user(user_type, username, full_name, email,
                                                user_image, password_hashed, phone_number, address, 
                                                age, specialty, pay_rate)
                        VALUES ('admin_user', :username, :full_name, :email, :user_image, :password,
                                :phone, :address, :age, :specialty, :payrate)'''
                try:
                    cur.execute(qry, {'username': username, 'full_name': full_name, 'email': email, 'user_image': user_image,
                                    'password':  password, 'phone': phone, 'address': address, 'age': age,
                                    'specialty': speciality, 'payrate': payrate})
                    connection.commit()
                except Exception as e:
                    print(f'The following error occured: {e}')
    def delete_user(self, username):
        with self.__connect() as connection:
            with connection.cursor() as cursor:
                qry='''DELETE FROM salon_user WHERE username=:username'''
                try:
                    cursor.execute(qry, username=username)
                    connection.commit()
                except Exception as e:
                    print(f'The following error occured: {e}')

            
    def get_members_cond(self, condition):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = f'''SELECT user_id,
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
                           WHERE {condition} ''' 
                    cursor.execute(qry)
                    rows = cursor.fetchall()
                    members_list = []
                    for pro in rows:
                        members_list.append(Member(*pro))
                    return members_list
        except Exception as e:
            print(f'Error retrieving member: {e}')


    def update_profile(self,username, new_password, full_name, email, phone_number, address, user_image):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = '''UPDATE salon_user
                            SET password_hashed = :new_password,
                                full_name = :full_name,
                                email = :email,
                                phone_number = :phone_number,
                                address = :address,
                                user_image = :user_image
                            WHERE username = :username'''
                    cursor.execute(qry,username=username,new_password=new_password,full_name=full_name,email=email,phone_number=phone_number,address=address,user_image=user_image)
                    connection.commit()
        except Exception as e:
            print(f'Error updating member: {e}')
 
    
    def update_profile_admin(self, user_id, user_type, username, full_name, new_password, email,
                         phone_number, address, age, speciality, pay_rate, user_image):
        try:
            with self.__connect() as connection:
                with connection.cursor() as c:
                    qry = '''UPDATE salon_user
                            SET user_type = :user_type,
                                username = :username,
                                full_name = :full_name,
                                password_hashed = :new_password,
                                email = :email,
                                phone_number = :phone_number,
                                address = :address,
                                age = :age,
                                specialty = :speciality,
                                pay_rate = :pay_rate,
                                user_image = :user_image
                            WHERE user_id = :user_id'''  # Added a comma after :pay_rate

                    info = [user_type,
                            username,
                            full_name,
                            new_password,
                            email,
                            phone_number,
                            address,
                            age,
                            speciality,
                            pay_rate,
                            user_image,
                            user_id]
                    c.execute(qry, info) 
                    connection.commit()
        except Exception as e:
            print(f'The following error occured: {e}')
    
    def get_active(self, username):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = '''SELECT is_active FROM salon_user WHERE username = :username'''
                    cursor.execute(qry,[username])
                    row = cursor.fetchone()
                    if row:
                        active = row[0]
                        return active
        except Exception as e:
            print(f'Error retrieving member: {e}')

    def set_active(self, username, active):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = '''UPDATE salon_user SET is_active=:active WHERE username = :username'''
                    cursor.execute(qry, [active,username])
                    connection.commit()
        except Exception as e:
            print(f'Error updating member: {e}')
    
    def get_flag(self, username):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
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
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = '''UPDATE salon_user SET status=:status WHERE username = :username'''
                    cursor.execute(qry, username=username, status=status)
                    connection.commit()
        except Exception as e:
            print(f'Error updating member: {e}')

    def appointments_cond(self, cond=''):
        '''method to get appointments under a certain condition'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    qry = f'''SELECT * FROM salon_appointment {cond}'''
                    cursor.execute(qry)
                    rows = cursor.fetchall()
                    appointments_list = []
                    for app in rows:
                        appointments_list.append(Appointment(*app))
                    return appointments_list
        except Exception as e:
            print(f'The following error occurred: {e}')            
    
# add new appointment to database
    def add_new_appointment(self, username, professional, service, venue, slot, date):
        '''  method to schedule a new appointment, data coming fro a user input form'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'''INSERT INTO salon_appointment (client_id, professional_id,
                                 service_id, slot, venue, date_appointment, client_name, professional_name, service_name)  
                                VALUES ((SELECT user_id FROM salon_user WHERE username = :username), 
                                        (SELECT user_id FROM salon_user WHERE username = :professional), 
                                        (SELECT service_id FROM salon_service WHERE service_name = :service), 
                                        :slot, :venue, :date_appointment,
                                        (SELECT full_name FROM salon_user WHERE username = :username),
                                        (SELECT full_name FROM salon_user WHERE username = :professional),
                                        :service)'''
                    info = {'username' : username, 
                            'professional': professional, 
                            'service': service, 
                            'slot': slot, 
                            'venue': venue, 
                            'date_appointment': date}
                    cursor.execute(sql, info)
                    connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

#edit appointment from database
    def edit_appointment(self, appointment_id, status, date_appointment, service, slot):
        '''  method to edit appointment from the database'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'''UPDATE salon_appointment SET status = :status, 
                                                            date_appointment = :date_appointment,  
                                                            service_id = (SELECT service_id FROM salon_service WHERE service_name = :service),
                                                            slot = :slot,
                                                            service_name = :service
                                                            WHERE appointment_id = :appointment_id'''
                    info = {'appointment_id' : appointment_id, 
                            'status' : status, 
                            'date_appointment' : date_appointment, 
                            'service' : service,
                            'slot' : slot,
                            'service' : service}
                    cursor.execute(sql, info)
                    connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')    

# add new report to database
    def add_new_report(self,user_id, appointment_id, title, client_report, professional_report):
        '''  method to schedule a new appointment, data coming fro a user input form'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'''INSERT INTO salon_report (user_id, appointment_id, title, client_report, professional_report) 
                                VALUES (:user_id,
                                        :appointment_id, 
                                        :title, 
                                        :client_report, 
                                        :professional_report)'''
                    info = {'user_id': user_id,'appointment_id' : appointment_id, 'title': title, 'client_report': client_report, 'professional_report': professional_report}
                    cursor.execute(sql, info)
                    connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

            
    def edit_report(self, report_id, new_client_report, new_professional_report):
        '''  method to edit existing report in database'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'''UPDATE salon_report
                                SET client_report = :client_report, professional_report = :professional_report
                                WHERE report_id = :report_id'''
                    info = {'report_id' : report_id, 'client_report': new_client_report, 'professional_report': new_professional_report}
                    cursor.execute(sql, info)
                    connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

    
    def get_appointment_reports(self, appointment_id):
        ''' method to list all reports of a specific appointment'''
        try:
            with self.__connect() as connection:
                with connection.cursor() as c:
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
            with self.__connect() as connection:
                with connection.cursor() as c:
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
                
    def delete_report(self, report_id):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'DELETE FROM salon_report WHERE report_id = :report_id'
                    info = {'report_id' : report_id}
                    cursor.execute(sql, info)
                    connection.commit()
        except Exception as e:
            print (f'The following error occured: {e}')

    def get_all_services(self):
        service_names = []
        try:
            with self.__connect() as connection:
                with connection.cursor() as c:
                    qry = '''
                        SELECT
                            service_name
                        FROM
                            salon_service
                    '''
                    c.execute(qry)
                    services = c.fetchall()
                    for service in services:
                        service_names.append(service[0])

                    # Process appointments as needed
                    return services
        except Exception as e:
            # Handle exceptions
            print(e)

    def get_services(self):
        ''' method to list all services  '''
        services = []
        try:
            with self.__connect() as connection:
                with connection.cursor() as c:
                    sql = 'SELECT * FROM salon_service'
                    c.execute(sql)
                    rows = c.fetchall()
                    return rows
        except Exception as e:
            print(e)

    def delete_appointment(self, appointment_id):
        try:
            with self.__connect() as connection:
                with connection.cursor() as cursor:
                    sql = f'DELETE FROM salon_appointment WHERE appointment_id = :appointment_id'
                    cursor.execute(sql, appointment_id=appointment_id)
                    connection.commit()
        except Exception as e:
            print(e)
            
    def get_all_logs(self):
        ''' method to list all logs '''
        logs = []
        try:
            with self.__connect() as connection:
                with connection.cursor() as c:
                    sql = f'SELECT * FROM salon_logs order by time_log DESC'
                    rows = c.execute(sql).fetchall()
                    return rows
        except Exception as e:
            print(e)    
#----------END of work area -----------

# if __name__ != '__main__':
    #import things 

        # ----------------------                   
        # ----------------------------
        #  1.	Create two global variables:
        # •	an instance of Database class that you call db.
db = Database()

# # 2.	Call run_sql_script on da1tabase.sql  if the script (database.py) is run in isolation.

# if __name__ == '__main__':
#     database.run_sql_script('schema.sql')
#     database.update_image("liliana2020", "michel.png")