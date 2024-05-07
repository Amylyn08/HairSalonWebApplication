from hairsalon_app.qdb.database import db

class Appointment:
    def __init__(self, appointment_id, status, approved, date_appointment, client_id, professional_id, service_id, slot, venue):
        self.appointment_id = appointment_id
        self.status = status
        self.approved = approved
        self.date_appointment = date_appointment
        self.client_id = client_id
        self.professional_id = professional_id
        self.service_id = service_id
        self.slot = slot
        self.venue = venue
        self.client_name = db.get_client_name(client_id)
        self.professional_name = db.get_professional_name(professional_id)
        self.service_name = db.get_service_name(service_id)