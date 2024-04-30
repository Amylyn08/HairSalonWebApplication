from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.report_view.forms import ReportForm
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import Database


report_bp = Blueprint('report_bp', __name__, template_folder='templates')
db = Database()


#route to create report
@report_bp.route('/report/', methods=['POST', 'GET'])
def create_report():
    form = ReportForm() 
    if form.validate_on_submit():
        db.add_new_report(form.appointment_id.data, form.title.data, form.client_report.data, form.professional_report.data, form.member_type.data)
        flash('Report sent', 'success')
        return redirect(url_for('report_bp.create_report'))
    flash('Invalid Inputs.' 'error')
    return render_template('report.html', form=form)

# #route for all appointments
# @report_bp.route("/all_appointments", methods=['GET'])
# def all_appointments(): #the id is the one for the note
#     #get apps from db
#     all_appointments = db.get_all_appointments()
     
#     if (len(all_appointments)!= 0):
#         return render_template("all_appointments.html", context = all_appointments)
        
#     return redirect(url_for("appointment_bp.create_appointment"))

# #route for all reports
# @report_bp.route("/all_appointments", methods=['GET'])
# def all_appointments(): #the id is the one for the note
#     #get apps from db
#     all_appointments = db.get_all_appointments()
     
#     if (len(all_appointments)!= 0):
#         return render_template("all_appointments.html", context = all_appointments)
        
#     return redirect(url_for("appointment_bp.create_appointment"))
