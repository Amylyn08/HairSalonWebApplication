from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.appointment_view.forms import AppointmentForm, AppointmentEditForm
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import db
import datetime


appointment_bp = Blueprint('appointment_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/appointment_view/static')


@appointment_bp.route('/appointment/', methods=['POST', 'GET'])
@login_required 
def create_appointment():
    form = AppointmentForm() #create form to add address to list
    if form.validate_on_submit():
        existing_apps = db.get_appointment_by_client_date(username=current_user.username, date=form.date.data)
        if existing_apps is None:       
            db.add_new_appointment(username=current_user.username,
                                   professional=form.professional.data,
                                   service=form.service.data,
                                   venue=form.venue.data,
                                   slot=form.slot.data,
                                   date=form.date.data)
        flash('Appointment scheduled', 'success')
        return redirect(url_for('appointment_bp.my_appointments', user_id=current_user.user_id))
    flash('Invalid Inputs.' 'error')
    return render_template('appointment.html', form=form)

#route for user's appointments
@appointment_bp.route("/my_appointments/<int:user_id>/", methods=['GET'])
@login_required
def my_appointments(user_id):
    #get apps from db
    my_appointments = db.get_my_appointments(user_id)
    for app in my_appointments:
        app.client_name = db.get_client_name(client_id=app.client_id)
        app.professional_name = db.get_professional_name(professional_id=app.professional_id)
        app.service_name = db.get_service_name(service_id=app.service_id)
    if (len(my_appointments)!= 0):
        return render_template("my_appointments.html", context = my_appointments)
    return redirect(url_for("appointment_bp.create_appointment"))

#route for all appointments
@appointment_bp.route("/all_appointments/", methods=['GET'])
def all_appointments(): #the id is the one for the note
    #get apps from db
    all_appointments = db.get_all_appointments() 
    for app in all_appointments:
        app.client_name = db.get_client_name(client_id=app.client_id)
        app.professional_name = db.get_professional_name(professional_id=app.professional_id)
        app.service_name = db.get_service_name(service_id=app.service_id)
    if (len(all_appointments)!= 0):
        return render_template("all_appointments.html", context = all_appointments)
    flash("No appointments to show", 'info')
    return redirect(url_for("appointment_bp.create_appointment"))

@appointment_bp.route("/all_appointments/sorted/<string:sorted_by>/", methods=['GET', 'POST'])
def sort_appointments(sorted_by):
        if sorted_by == 'Date':
            all_appointments = db.get_all_appointments_date_desc()
        if sorted_by == 'fullname':
            all_appointments = db.get_all_appointments_fullname_asc()
        if sorted_by == 'Slot':
            pass
        if sorted_by == 'Professional':
            all_appointments = db.get_all_appointments_profname()
        if sorted_by == 'Client':
            all_appointments = db.get_all_appointments_clientname()
        if sorted_by == 'Pending':
            all_appointments = db.get_all_appointments_pending()
        if sorted_by == 'Approved':
            all_appointments = db.get_all_appointments_approved()
        if sorted_by == 'Completed':
            all_appointments = db.get_all_appointments_completed()
        if sorted_by == 'Cancelled':
            all_appointments = db.get_all_appointments_cancelled()
        return render_template("all_appointments.html", context = all_appointments)
#route to edit appointment
@appointment_bp.route("/edit_appointment/<int:appointment_id>", methods=['POST', 'GET'])
def edit_appointment(appointment_id):
    form = AppointmentEditForm()
    appointment = db.get_appointment_by_id(appointment_id)
    form.date.data = appointment.date_appointment
    form.slot.data = appointment.slot

    if form.validate_on_submit():
        if True:
            db.edit_appointment(appointment_id, form.status.data, form.date.data, form.service.data, )
            flash('Appointment edited', 'success')
            return redirect(url_for('appointment_bp.edit_appointment', appointment_id=appointment_id))
        
    flash('Invalid Inputs.' 'error')
    return render_template('edit_appointment.html', form=form, appointment = appointment)

@appointment_bp.route("/appointment/<int:appointment_id>", methods=['GET'])
@login_required
def specific_appointment(appointment_id):
    appointment = db.get_appointment(appointment_id)
    reports = db.get_appointment_reports(appointment_id)
    appointment.client_name = db.get_client_name(client_id= appointment.client_id)
    appointment.professional_name = db.get_professional_name(professional_id=appointment.professional_id)
    appointment.service_name = db.get_service_name(service_id=appointment.service_id)
    if appointment is None:
        flash('Appointment not found', 'error')
        return redirect(url_for("appointment_bp.all_appointments"))
    return render_template("specific_appointment.html", 
                           appointment = appointment,
                            reports = reports,
                            reports_length = len(reports))


