from flask import Blueprint, flash, redirect, render_template, url_for


appointment_bp = Blueprint('appointment', __name__, template_folder='templates')
#db = Database()

@appointment_bp.route('/')
@appointment_bp.route('/appointment/')
def home():
    return render_template('appointment.html')