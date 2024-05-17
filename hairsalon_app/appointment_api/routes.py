from flask import Blueprint, request
from flask_restful import Api, Resource
from hairsalon_app.qdb.database import db
from oracledb import Date


api_bp = Blueprint('api_bp', __name__)
api = Api(api_bp)

class Appointments_API(Resource):
    ''' Class for appointments API s '''
    def get(self):
        ''' Method to get all appointments  '''
        all_appointments = db.appointments_cond()
        return {"length": len(all_appointments),
                "all_appointment": [appointment.to_dict() for appointment in all_appointments]}, 200
    
    def post(self):
        ''' Method to create an appointment '''
        try:
            data = request.get_json(force=True)
            db.add_new_appointment(
                data['username'], 
                data['professional'], 
                data['service'], 
                data['venue'], 
                data['slot'], 
                Date.fromisoformat(data['date'])
            )
            return {'message': 'Appointment created successfully'}, 201
        except KeyError as e:
            return {'message': f'Missing key in request data: {e}'}, 400
        except ValueError as e:
            return {'message': f'Invalid date format: {e}'}, 400
        except Exception as e:
            return {'message': f'Error creating appointment: {e}'}, 500

class Appointment_API(Resource):
    ''' Method to get a specific appointment according to an appointment ID  '''
    def get(self, appointment_id):
        appointment =  db.appointments_cond(cond=f"WHERE appointment_id = {appointment_id}")[0]
        if appointment:
            return appointment.to_dict(), 200
        else:
            return {'message': 'Appointment not found'}, 404
    
    def delete(self, appointment_id):
        ''' Method to delete an appointment using an ID '''
        if  db.appointments_cond(cond=f"WHERE appointment_id = {appointment_id}")[0]:
            db.delete_appointment(appointment_id)
            return f'Appointment {appointment_id} deleted', 204
        else:
            return f'Appointment {appointment_id} not found', 404

api.add_resource(Appointment_API, '/api/appointment/<int:appointment_id>/')
api.add_resource(Appointments_API, '/api/appointments/')
