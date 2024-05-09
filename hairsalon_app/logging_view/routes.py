from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from hairsalon_app.appointment_view.forms import AppointmentForm, AppointmentEditForm
from hairsalon_app.appointment_view.appointment import Appointment
from hairsalon_app.qdb.database import db
import datetime


log_bp = Blueprint('log_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/appointment_view/static')

#route for all logs
@log_bp.route("/all_logs/", methods=['GET'])
def all_log():
    #get logs from db
    all_logs = db.get_all_logs() 
    if (len(all_logs)!= 0):
        return render_template("all_logs.html", context = all_logs)
    flash("No logs to show", 'info')
    return redirect(url_for("log_bp.all_logs"))