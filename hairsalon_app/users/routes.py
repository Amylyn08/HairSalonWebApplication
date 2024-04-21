#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, url_for, redirect, render_template
from hairsalon_app.qdb.database import Database

#Create an instance of Database
db = Database()

#Create a blueprint
users_bp = Blueprint("user",__name__,template_folder='templates')

#List of users
users = []

#Generates all the notes
@users_bp.route("/profile")
def user_list():
    """Function for listing all the users."""
    
