
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
        self.client_name = 0
        self.professional_name=0
        self.service_name =0
