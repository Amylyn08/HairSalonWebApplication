from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.report_view.forms import ReportForm, ReportEdit
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

#route for all reports
@report_bp.route("/all_reports/", methods=['GET'])
def all_reports(): #the id is the one for the note
    #get reports from db
    all_reports = db.get_all_reports()
     
    if (len(all_reports)!= 0):
        return render_template("all_reports.html", context = all_reports)
        
    return redirect(url_for("report_bp.create_report"))

#route to create report
@report_bp.route('/edit_report/<int:report_id>', methods=['POST', 'GET'])
def edit_report(report_id):
    if current_user.user_id == db.get_report_by_id(report_id).user_id:
        form = ReportEdit() 
        if form.validate_on_submit():
            db.edit_report(report_id, form.client_report.data, form.professional_report.data)
            flash('Report sent', 'success')
            return redirect(url_for('report_bp.all_reports'))
    flash('Invalid Inputs.' 'error')
    return render_template('edit_report.html', form=form)

# #route for all reports
# @report_bp.route("/all_appointments", methods=['GET'])
# def all_appointments(): #the id is the one for the note
#     #get apps from db
#     all_appointments = db.get_all_appointments()
     
#     if (len(all_appointments)!= 0):
#         return render_template("all_appointments.html", context = all_appointments)
        
#     return redirect(url_for("appointment_bp.create_appointment"))
