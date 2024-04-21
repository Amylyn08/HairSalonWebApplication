from flask import Blueprint, flash, redirect, render_template, url_for
from hairsalon_app.appointment_view.forms import AppointmentForm
from hairsalon_app.appointment_view.appointment import Appointment


appointment_bp = Blueprint('appointment', __name__, template_folder='templates')
#db = Database()


@appointment_bp.route('/')
@appointment_bp.route('/appointment/', methods=['POST', 'GET'])
def create_appointment():
    appointment_form = AppointmentForm() #create form to add address to list

    if appointment_form.validate_on_submit():
        flash('Appointment scheduled', 'success')

    #return render_template("owners.html", context = owners, form = owners_form)
    return render_template('appointment.html', form = appointment_form)

#route for a specific note
@appointment_bp.route("/my_appointments")
def my_appointments(): #the id is the one for the note
    #mimic db for now
    my_appointments = [
        Appointment(1, "bob", "04-24-2024"),
        Appointment(2, "bob", "04-27-2024"),
        Appointment(3, "bob", "04-21-2024"),
    ]
     
    if (len(my_appointments)!= 0):
        return render_template("my_appointments.html", context = my_appointments)
        
    return redirect(url_for("create_appointment"))
