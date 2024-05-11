from flask import Blueprint, abort, current_app, flash, make_response, url_for, redirect, render_template,request
from hairsalon_app.qdb.database import db

service_bp = Blueprint("service_bp",__name__,template_folder='main_view/templates', static_folder='static', static_url_path='/services/static')

@service_bp.route('/home/services')
def get_services():
    """Function for listing all the services."""
    services = db.get_all_services()  #
    return services 