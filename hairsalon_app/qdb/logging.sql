DROP TABLE SALON_LOGS

CREATE TABLE SALON_LOGS
(
    action VARCHAR2(15) NOT NULL,
    table_name VARCHAR2(30) NOT NULL,
    user_id NUMBER,
    time_log TIMESTAMP
);

CREATE OR REPLACE TRIGGER trigger_appointment_insert
  AFTER INSERT ON SALON_APPOINTMENT
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'INSERT', 'SALON_APPOINTMENT', :NEW.client_id, SYSTIMESTAMP);
 END;
 
 /
 
CREATE OR REPLACE TRIGGER trigger_appointment_update
  AFTER UPDATE ON SALON_APPOINTMENT
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'UPDATE', 'SALON_APPOINTMENT', :NEW.client_id, SYSTIMESTAMP);
 END;
 
 /
 
CREATE OR REPLACE TRIGGER trigger_user_insert
  AFTER INSERT ON SALON_USER
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'INSERT', 'SALON_USER', :NEW.user_id, SYSTIMESTAMP);
 END;
 
 /
 
CREATE OR REPLACE TRIGGER trigger_user_update
  AFTER UPDATE ON SALON_USER
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'UPDATE', 'SALON_USER', :NEW.user_id, SYSTIMESTAMP);
 END;
 
 /
 
 CREATE OR REPLACE TRIGGER trigger_report_insert
  AFTER INSERT ON SALON_REPORT
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'INSERT', 'SALON_REPORT', :NEW.user_id, SYSTIMESTAMP);
 END;
 
 /
 
CREATE OR REPLACE TRIGGER trigger_report_update
  AFTER UPDATE ON SALON_REPORT
  FOR EACH ROW
BEGIN
    INSERT INTO SALON_LOGS
      VALUES( 'UPDATE', 'SALON_REPORT', :NEW.user_id, SYSTIMESTAMP);
 END;