#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, flash, url_for, redirect, render_template
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
    users_clients = db.get_users_clients()
    return render_template('allUsers.html', clients =users_clients)

@users_bp.route("/profile/professional")
def user_list_professional():
    """Function for listing all the users."""
    users_professionals= db.get_users_professional()
    return render_template('allUsers.html', profesionnals = users_professionals)

@users_bp.route("/profile/<username>")
def client_name(username):
    """Function for finding a client by his username."""
    users_clients = db.get_users_clients()
    for client in users_clients:
        if client.username == username:
            return render_template('client.html', clients = client)
    flash("Sorry but this address doesn't exist !","errors_class")
    return redirect(url_for('user_list_client'))

@users_bp.route("/profile/<username>")
def professional_name(username):
    """Function for finding a client by his username."""
    users_professionals = db.get_users_professional()
    for professional in users_professionals:
        if professional.username == username:
            return render_template('professional.html', professionals= professional)
    flash("Sorry but this address doesn't exist !","errors_class")
    return redirect(url_for('user_list_professional'))