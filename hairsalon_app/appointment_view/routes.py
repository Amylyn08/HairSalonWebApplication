from flask import Blueprint, flash, redirect, render_template, request, url_for
import flask
from flask_login import current_user, login_required
from hairsalon_app.appointment_view.forms import AppointmentForm, AppointmentEditForm, AppointmentFormPro
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import db
from markupsafe import escape


appointment_bp = Blueprint('appointment_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/appointment_view/static')


@appointment_bp.route('/appointment/', methods=['POST', 'GET'])
@login_required 
def create_appointment():
    pros_list = db.get_members_cond(condition="user_type='professional'")
    client_list = db.get_members_cond(condition="user_type='client'")
    service_list = db.services_cond()
    
    if current_user.user_type == 'professional' or 'admin' in current_user.user_type:
        formPro = AppointmentFormPro()
        formPro.client.choices = [(c.username, c.username) for c in client_list]
        formPro.service.choices = [(s[1], s[1]) for s in service_list]
        form = formPro
    else:
        formClient = AppointmentForm()
        formClient.professional.choices = [(p.username, p.username) for p in pros_list]
        formClient.service.choices = [(s[1], s[1]) for s in service_list]
        form = formClient

    if form.validate_on_submit():
        existing_apps = db.appointments_cond(cond=f"WHERE date_appointment = TO_DATE('{form.date.data}', 'YYYY-MM-DD') AND client_name = '{current_user.full_name}'")    
        if len(existing_apps) == 0:       
            if current_user.user_type == 'professional' or 'admin' in current_user.user_type:
                user_data = form.client.data
                pro_data = current_user.username
            else:
                user_data=current_user.username
                pro_data = form.professional.data
            db.add_new_appointment(
                username=user_data,
                professional=pro_data,
                service=form.service.data,
                venue=form.venue.data,
                slot=form.slot.data,
                date=form.date.data
            )
            flash('Appointment scheduled', 'success')
            return redirect(url_for('appointment_bp.my_appointments', user_id=current_user.user_id))
        else:
            flash('This appointment already exists.', 'error')

    return render_template('appointment.html', form=form)


#route for user's appointments
@appointment_bp.route("/my_appointments/<int:user_id>/", methods=['GET'])
@login_required
def my_appointments(user_id):
    if user_id != current_user.user_id:
        flash("Not your appointments to view", 'info')
    my_appointments = db.appointments_cond(cond=f"WHERE client_id={user_id} OR professional_id={user_id}")
    if (len(my_appointments)!= 0):
        return render_template("my_appointments.html", context = my_appointments)
    flash("No appointments to show", 'info')
    return redirect(url_for("appointment_bp.create_appointment"))

#route for all appointments
@appointment_bp.route("/all_appointments/", methods=['GET'])
def all_appointments():
    all_appointments = db.appointments_cond()
    if (len(all_appointments)!= 0):
        return render_template("all_appointments.html", context = all_appointments)
    flash("No appointments to show", 'info')
    return redirect(url_for("appointment_bp.create_appointment"))

@appointment_bp.route("/all_appointments/sorted/<string:sorted_by>/", methods=['GET', 'POST'])
def sort_appointments(sorted_by):
        sorted_by = escape(sorted_by)
        if sorted_by == 'Date':
            all_appointments = db.appointments_cond(cond="ORDER BY date_appointment DESC")
        if sorted_by == 'Slot':
            all_appointments = db.appointments_cond(cond="ORDER BY TO_NUMBER(SUBSTR(slot, 1, INSTR(slot, '-') - 1))")
        if sorted_by == 'Professional':
            all_appointments = db.appointments_cond(cond="ORDER BY professional_name ASC")
        if sorted_by == 'Client':
            all_appointments = db.appointments_cond(cond="ORDER BY client_name ASC")
        if sorted_by == 'Pending':
            all_appointments = db.appointments_cond(cond="WHERE status = 'pending'")
        if sorted_by == 'Approved':
            all_appointments = db.appointments_cond(cond="WHERE status = 'approved'")
        if sorted_by == 'Completed':
            all_appointments = db.appointments_cond(cond="WHERE status = 'completed'")
        if sorted_by == 'Cancelled':
            all_appointments = db.appointments_cond(cond="WHERE status = 'cancelled'")
        return render_template("all_appointments.html", context = all_appointments)
#route to edit appointment
@appointment_bp.route("/edit_appointment/<int:appointment_id>", methods=['POST', 'GET'])
@login_required 
def edit_appointment(appointment_id):
    app = db.appointments_cond(cond=f"WHERE appointment_id={appointment_id} AND (client_id={current_user.user_id} or professional_id={current_user.user_id})")
    if not app and (current_user.user_type != 'admin_super' and current_user.user_type != 'admin_appoint'):
        flash('Not your appointment to view.', 'info')
        return redirect(url_for("appointment_bp.all_appointments"))
    service_list = db.services_cond()
    appointment = db.appointments_cond(cond=f"WHERE appointment_id = {appointment_id}")[0]
    form = AppointmentEditForm()
    form.service.choices = [(s[1], s[1]) for s in service_list]
    if flask.request.method == 'GET':
        form.date.data = appointment.date_appointment
        form.slot.data = appointment.slot
        form.service.data = appointment.service_name
        form.status.data = appointment.status
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            db.edit_appointment(appointment_id, form.status.data, form.date.data, form.service.data, form.slot.data)
            flash('Appointment edited', 'success')
            return redirect(url_for('appointment_bp.specific_appointment', appointment_id=appointment_id))
            
        else:
            flash('Invalid Inputs.', 'error')
        
    return render_template('edit_appointment.html', form=form, appointment=appointment)


@appointment_bp.route("/appointment/<int:appointment_id>", methods=['GET'])
@login_required
def specific_appointment(appointment_id):
    appointment =  db.appointments_cond(cond=f"WHERE appointment_id = {appointment_id}")[0]
    reports = db.reports_cond(cond=f"WHERE appointment_id = {appointment_id}")
    if appointment is None:
        flash('Appointment not found', 'error')
        return redirect(url_for("appointment_bp.all_appointments"))
    return render_template("specific_appointment.html", 
                           appointment = appointment,
                            reports = reports,
                            reports_length = len(reports))
@appointment_bp.route("/delete_appointment/<int:appointment_id>", methods=['GET','POST'])
@login_required 
def delete_appointment(appointment_id):
    app = db.appointments_cond(cond=f"WHERE appointment_id={appointment_id} AND (client_id={current_user.user_id} or professional_id={current_user.user_id})")
    if not app and (current_user.user_type != 'admin_super' and current_user.user_type != 'admin_appoint'):
        flash('Not your appointment to delete', 'info')
        return redirect(url_for("appointment_bp.all_appointments"))
    appointment =  db.appointments_cond(cond=f"WHERE appointment_id = {appointment_id}")[0]
    if appointment is not None:
        db.delete_appointment(appointment_id)
        flash('Appointment deleted successfully','success')
    else:
        flash('Appointment not found', 'error')
    return redirect(url_for('appointment_bp.all_appointments'))

