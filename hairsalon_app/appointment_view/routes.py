from flask import Blueprint, flash, redirect, render_template, url_for
from hairsalon_app.appointment_view.forms import AppointmentForm


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