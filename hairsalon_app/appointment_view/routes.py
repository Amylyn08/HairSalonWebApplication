from flask import Blueprint, flash, redirect, render_template, url_for
from hairsalon_app.appointment_view.forms import AppointmentForm
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import Database


appointment_bp = Blueprint('appointment_bp', __name__, template_folder='templates')
db = Database()


@appointment_bp.route('/appointment/', methods=['POST', 'GET'])
def create_appointment():
    appointment_form = AppointmentForm() #create form to add address to list

    if appointment_form.validate_on_submit():
        flash('Appointment scheduled', 'success')

    #return render_template("owners.html", context = owners, form = owners_form)
    return render_template('appointment.html', form = appointment_form)

#route for user's appointments
@appointment_bp.route("/my_appointments", methods=['GET'])
def my_appointments():
    #get apps from db
    my_appointments = db.get_my_appointments()
     
    if (len(my_appointments)!= 0):
        return render_template("my_appointments.html", context = my_appointments)
        
    return redirect(url_for("create_appointment"))

#route for all appointments
@appointment_bp.route("/all_appointments", methods=['GET'])
def all_appointments(): #the id is the one for the note
    #get apps from db
    all_appointments = db.get_all_appointments()
     
    if (len(all_appointments)!= 0):
        return render_template("all_appointments.html", context = all_appointments)
        
    return redirect(url_for("appointment_bp.create_appointment"))
