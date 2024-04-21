#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, url_for, redirect, render_template
from hairsalon_app.qdb.database import Database

#Create an instance of Database
db = Database()

#Create a blueprint
users_bp = Blueprint("user",__name__,template_folder='templates')

#List of users
users_clients= []
users_professionals =[]

#Generates all the notes
@users_bp.route("/profile/client")
def user_list_client():
    """Function for listing all the users."""
    users = db.get_users_clients()
    return render_template('client.html')

@users_bp.route("/profile/professional")
def user_list_professional():
    """Function for listing all the users."""
    users = db.get_users_professional()
    return render_template('professional.html')