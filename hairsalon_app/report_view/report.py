class Report:
    def __init__(self, report_id, user_id, appointment_id, date_report, title, client_report, professional_report):
        self.report_id = report_id
        self.user_id = user_id
        self.appointment_id = appointment_id
        self.date_report = date_report
        self.title = title
        self.client_report = client_report
        self.professional_report = professional_report