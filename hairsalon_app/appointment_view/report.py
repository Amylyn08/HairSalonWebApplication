class Report:
    def __init__(self, report_id, appointment_id, date_report, member_type, title, client_report, professional_report):
        self.report_id = report_id
        self.appointment_id = appointment_id
        self.date_report = date_report
        self.member_type = member_type
        self.title = title
        self.client_report = client_report
        self.professional_report = professional_report