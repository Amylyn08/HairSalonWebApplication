from flask import Blueprint, render_template
from hairsalon_app.qdb.database import db


main_bp = Blueprint('main_bp', __name__, template_folder='templates',static_folder='static', static_url_path='/main_view/static')

@main_bp.route('/about')
def about():
    """Return the about page."""
    return render_template('about.html')

@main_bp.route('/home/')
@main_bp.route('/')
def home():
    """Return the home page."""
    list_services = db.services_cond()
    return render_template('home.html',services=list_services)

@main_bp.route('/api/')
def api_docs():
    """Return the api docs page."""
    return render_template('api_docs.html')




