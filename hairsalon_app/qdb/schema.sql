DROP TABLE salon_report;
DROP TABLE salon_appointment;
DROP TABLE salon_service;
DROP TABLE salon_user;



-- Create table for salon_professional
CREATE TABLE salon_user (
    user_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    is_active NUMBER(1) default(0), --active or deactivated
    status NUMBER(1) default(0), --flagged or warned.
    user_type VARCHAR2(15) default ('client'), --client, professional, admin_user, admin_appoint, or admin_super.
    username VARCHAR2(30) NOT NULL UNIQUE,
    full_name VARCHAR2(100) default null,
    email VARCHAR2(120) NOT NULL,
    user_image VARCHAR2(30),
    password_hashed VARCHAR2(80) NOT NULL,
    phone_number VARCHAR2(80) NOT NULL,
    address VARCHAR2(100) default NULL,
    age NUMBER(3) NOT NULL,
    pay_rate DECIMAL(5, 2) default(NULL),
    specialty VARCHAR2(15) default(NULL),
    
    CONSTRAINT user_pk PRIMARY KEY (user_id)
);

---Insert Valuesfor user member
INSERT INTO salon_user(username, full_name, email, user_image ,password_hashed, phone_number, address, age) 
VALUES('iana_life','Iana Feniuc','ianafeniuc@gmail.com','user.png','sjkdhuvb','514-567-1567','2135 Boul Russeau',19);

-- Create table for salon_service
CREATE TABLE salon_service (
    service_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    service_name VARCHAR2(35) NOT NULL,
    service_duration NUMBER(2) NOT NULL,
    service_price NUMBER(5, 2) NOT NULL,
    service_materials VARCHAR2(35) NOT NULL,
    
    CONSTRAINT service_pk PRIMARY KEY (service_id)
);

-- Create table for salon_appointment
CREATE TABLE salon_appointment (
    appointment_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    status VARCHAR2(10) default('pending'),
    approved NUMBER(1) default(1),
    date_appointment DATE default sysdate,
    client_id NUMBER NOT NULL,
    professional_id NUMBER NOT NULL,
    service_id NUMBER NOT NULL,
    slot VARCHAR2(10) default ('9-10'),
    venue VARCHAR(20) default ('cmn_room'),
    
    CONSTRAINT appointment_pk PRIMARY KEY (appointment_id),
    CONSTRAINT appointment_clientfk FOREIGN KEY (client_id) 
        REFERENCES salon_user(user_id),
    CONSTRAINT appointment_professionalfk FOREIGN KEY (professional_id)
        REFERENCES salon_user(user_id),
    CONSTRAINT appointment_sevicefk FOREIGN KEY (service_id) 
        REFERENCES salon_service(service_id)
);

-- Create table for salon_report
CREATE TABLE salon_report(
    report_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    appointment_id NUMBER NOT NULL,
    date_report DATE default sysdate,
    member_type NUMBER(1) NOT NULL,
    title VARCHAR2(50) NOT NULL,
    client_report VARCHAR2(500),
    professional_report VARCHAR2(500),
    
    CONSTRAINT report_pk PRIMARY KEY (report_id),
    CONSTRAINT report_fk FOREIGN KEY (appointment_id)
        REFERENCES Salon_Appointment(appointment_id)
);

INSERT INTO salon_user(user_type, username,full_name, email, user_image,password_hashed, phone_number, address, age)
    VALUES('admin_user','user_manager1', 'ADMIN_USER', 'saloon.adminuser@gmail.com', 'adminpfp.png', '123', '5142222222', '5000 street 1 Canada', 100);

INSERT INTO salon_user(user_type, username,full_name, email, user_image,password_hashed, phone_number, address, age)
    VALUES('admin_super','nasr', 'ADMIN_SUPER', 'saloon.adminuser@gmail.com', 'adminpfp.png', '123', '5142222222', '5000 street 1 Canada', 100);

INSERT INTO salon_user(user_type, username,full_name, email, user_image,password_hashed, phone_number, address, age)
    VALUES('admin_appoint','appoint_manager1', 'ADMIN_APPOINT', 'saloon.admin@gmail.com', 'adminpfp.png', '456', '5142222222', '5000 street 1 Canada', 100);

SELECT  user_type,username,full_name, email, user_image, password_hashed, phone_number,address,age,specialty,pay_rate FROM SALON_USER WHERE username='nasr';