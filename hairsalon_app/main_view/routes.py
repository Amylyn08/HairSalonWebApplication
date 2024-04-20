from flask import Blueprint, flash, redirect, render_template, url_for


main_bp = Blueprint('main', __name__, template_folder='templates')
#db = Database()

@main_bp.route('/')
@main_bp.route('/home/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')