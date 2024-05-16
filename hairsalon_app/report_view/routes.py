from flask import Blueprint, flash, redirect, render_template, url_for
import flask
from flask_login import current_user, login_required
from hairsalon_app.report_view.forms import ReportForm, ReportEdit
from hairsalon_app.qdb.database import db


report_bp = Blueprint('report_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/report_view/static')



#route to create report
@report_bp.route('/report/<int:appointment_id>/', methods=['POST', 'GET'])
@login_required 
def create_report(appointment_id):
    form = ReportForm() 
    if form.validate_on_submit():
        db.add_new_report(current_user.user_id, appointment_id, form.title.data, form.client_report.data, form.professional_report.data)
        flash('Report sent', 'success')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=appointment_id))
    flash('Invalid Inputs.' 'error')
    return render_template('report.html', form=form)

#route to create report
@report_bp.route('/edit_report/<int:report_id>', methods=['POST', 'GET'])
@login_required 
def edit_report(report_id):
    report = db.reports_cond(cond=f'''WHERE 
                                            salon_report.APPOINTMENT_ID IN (
                                                SELECT APPOINTMENT_ID FROM SALON_APPOINTMENT 
                                                WHERE CLIENT_ID = {current_user.user_id} 
                                                OR PROFESSIONAL_ID = {current_user.user_id}
                                            )''')[0]
    if not report:
        flash('Report not found, or not your report.' 'info')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=report.appointment_id))
    form = ReportEdit() 
    if form.validate_on_submit():
        if current_user.user_type == 'client':
            client_report = form.client_report.data
            pro_report = report.professional_report
        elif current_user.user_type == 'professional':
            client_report = report.client_report.data
            pro_report = form.professional_report.data
        else:
            client_report = form.client_report.data        
            pro_report = form.professional_report.data
        db.edit_report(report_id, client_report, pro_report)
        flash('Report sent', 'success')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=report.appointment_id))
    flash('Invalid Inputs.' 'error')
    return render_template('edit_report.html', form=form, report=report)

@report_bp.route('/delete_report/<int:report_id>/<int:appointment_id>/', methods=['POST', 'GET'])
@login_required 
def delete_report(report_id, appointment_id):
    report = db.reports_cond(cond=f"WHERE report_id = {report_id} AND user_id = {current_user.user_id}")[0]
    if not report:
        flash('Report not found, or not your report.' 'info')
        return redirect(url_for('appointment_bp.specific_appointment', appointment_id=report.appointment_id))
    db.delete_report(report_id)
    flash('Report deleted','success')
    return redirect(url_for('appointment_bp.specific_appointment', appointment_id=appointment_id))


