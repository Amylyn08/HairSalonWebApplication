from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.appointment_view.forms import AppointmentForm, AppointmentEditForm
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import Database
import datetime


appointment_bp = Blueprint('appointment_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/appointment_view/static')
db = Database()


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
@appointment_bp.route("/my_appointments/<int:user_id>", methods=['GET'])
@login_required
def my_appointments(user_id):
    #get apps from db
    my_appointments = db.get_my_appointments(user_id)
     
    if (len(my_appointments)!= 0):
        return render_template("my_appointments.html", context = my_appointments)
        
    return redirect(url_for("appointment_bp.create_appointment"))

#route for all appointments
@appointment_bp.route("/all_appointments/", methods=['GET'])
def all_appointments(sortbydate = None): #the id is the one for the note
    #get apps from db
    all_appointments = db.get_all_appointments()     
    if (len(all_appointments)!= 0 and sortbydate == "sortbydate"):
        return render_template("all_appointments.html", context = all_appointments)
        
    return redirect(url_for("appointment_bp.create_appointment"))

@appointment_bp.route("/all_appointments/sorted/<string: sorted_by>/", methods=['GET', 'POST'])
def sort_appointments(sorted_by):
        if sorted_by == 'Date':
            all_appointments = db.get_all_appointments_date_desc()
        if sorted_by == 'Slot':
            pass
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
    if appointment is None:
        flash('Appointment not found', 'error')
        return redirect(url_for("appointment_bp.all_appointments"))
    return render_template("specific_appointment.html", 
                           appointment = appointment,
                            reports = reports,
                            reports_length = len(reports))


