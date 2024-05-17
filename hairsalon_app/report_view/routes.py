from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.report_view.forms import ReportForm, ReportEdit
from hairsalon_app.qdb.database import db


report_bp = Blueprint('report_bp', __name__, template_folder='templates', 
                      static_folder='static', static_url_path='/report_view/static')



#route to create report
@report_bp.route('/report/<int:appointment_id>/', methods=['POST', 'GET'])
@login_required 
def create_report(appointment_id):
    '''Creates a new report with some permissions given an appointment.'''
    if current_user.user_type == 'professional' or \
          current_user.user_type == 'client':
        app = db.appointments_cond(cond=f'''WHERE appointment_id = {appointment_id}
                                        AND (client_id = {current_user.user_id} or
                                        professional_id = {current_user.user_id})''')
    elif current_user.user_type == 'admin_super' or \
        current_user.user_type == 'admin_appoint':
        app = db.appointments_cond(cond=f'''WHERE appointment_id = {appointment_id}''')
    else:
        flash('You are not permitted to create a report for this appointment.', 'info')
        return redirect(url_for('appointment_bp.all_appointments'))
    if not app:
        flash('The appointment does not exist or is not yours', 'error')
        return redirect(url_for('appointment_bp.all_appointments'))
    report = db.reports_cond(cond=f"WHERE appointment_id = {appointment_id}")
    if report:
        flash("A report already exist for this appointment", 'info')
        return redirect(url_for('appointment_bp.all_appointments'))
    form = ReportForm() 
    if form.validate_on_submit():
        db.add_new_report(current_user.user_id, 
                          appointment_id, 
                          form.title.data, 
                          form.client_report.data, 
                          form.professional_report.data)
        flash('Report sent', 'success')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=appointment_id))
    flash('Invalid Inputs.' 'error')
    return render_template('report.html', form=form)

#route to create report
@report_bp.route('/edit_report/<int:report_id>/', methods=['POST', 'GET'])
@login_required 
def edit_report(report_id):
    '''Edits a report given an ID, with some validations.'''
    if current_user.user_type == 'client' or \
        current_user.user_type == 'professional':
        report = db.reports_cond(cond=f'''WHERE 
                                                salon_report.APPOINTMENT_ID IN (
                                                    SELECT APPOINTMENT_ID FROM SALON_APPOINTMENT 
                                                    WHERE CLIENT_ID = {current_user.user_id} 
                                                    OR PROFESSIONAL_ID = {current_user.user_id}
                                                ) AND report_id = {report_id}''')
    elif current_user.user_type != 'admin_user':
        report = db.reports_cond(cond=f'''WHERE report_id = {report_id}''')
    else:
        flash("You don't have permissions to edit this report.", 'error')
        return redirect(url_for('appointment_bp.all_appointments'))
    if not report:
        flash('Report not found, or not your report.', 'info')
        return redirect(url_for('appointment_bp.all_appointments'))
    form = ReportEdit() 
    if form.validate_on_submit():
        if current_user.user_type == 'client':
            client_report = form.client_report.data
            pro_report = report[0].professional_report
        elif current_user.user_type == 'professional':
            client_report = report[0].client_report
            pro_report = form.professional_report.data
        else:
            client_report = form.client_report.data        
            pro_report = form.professional_report.data
        db.edit_report(report_id, client_report, pro_report)
        flash('Report sent', 'success')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=report[0].appointment_id))
    flash('Invalid Inputs.' 'error')
    return render_template('edit_report.html', form=form, report=report[0])

@report_bp.route('/delete_report/<int:report_id>/<int:appointment_id>/', methods=['POST', 'GET'])
@login_required 
def delete_report(report_id, appointment_id):
    '''Method to delete a report given a report_id and appointment_id for page rendering.'''
    if current_user.user_type == 'client' or \
            current_user.user_type == 'professional':
            report = db.reports_cond(cond=f'''WHERE 
                                                    salon_report.APPOINTMENT_ID IN (
                                                        SELECT APPOINTMENT_ID FROM SALON_APPOINTMENT 
                                                        WHERE CLIENT_ID = {current_user.user_id} 
                                                        OR PROFESSIONAL_ID = {current_user.user_id}
                                                    ) AND report_id = {report_id}''')
    elif current_user.user_type != 'admin_user':
        report = db.reports_cond(cond=f'''WHERE report_id = {report_id}''')
    else:
        flash("You don't have permissions to delete this report.", 'error')
        return redirect(url_for('appointment_bp.all_appointments'))
    if not report:
        flash('Report not found, or not your report.', 'info')
        return redirect(url_for('appointment_bp.all_appointments'))
    db.delete_report(report_id)
    flash('Report deleted','success')
    return redirect(url_for('appointment_bp.specific_appointment', appointment_id=appointment_id))


