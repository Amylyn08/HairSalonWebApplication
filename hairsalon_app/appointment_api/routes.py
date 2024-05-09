from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from hairsalon_app.qdb.database import db
from oracledb import Date
api_bp = Blueprint('api_bp', __name__)
api = Api(api_bp)

class Appointments_API(Resource):
    def get(self):
        all_appointments = db.get_all_appointments()
        return {"length": len(all_appointments),
                "all_appointment": [appointment.to_dict() for appointment in all_appointments]}, 200
    
    def post(self):
        data = request.json
        db.add_new_appointment(data['username'], 
                               data['professional'], 
                               data['service'], 
                               data['venue'], 
                               data['slot'], 
                               Date.fromisoformat(data['date'].split(' ')[0]))
        return self.get(), 201

class Appointment_API(Resource):
    def get(self, appointment_id):
        appointment = db.get_appointment_by_id(appointment_id)
        if appointment:
            return appointment.to_dict(), 200
        else:
            return {'message': 'Appointment not found'}, 404
    
    def delete(self, appointment_id):
        db.delete_appointment(appointment_id)
        return {'message': f'Appointment {appointment_id} deleted'}, 204

api.add_resource(Appointment_API, '/api/appointment/<int:appointment_id>/')
api.add_resource(Appointments_API, '/api/appointments/')
