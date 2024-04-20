from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager
from hairsalon_app.config import ConfigProd
from hairsalon_app.users.User import User


def create_app(config = ConfigProd):

    #Creating flask app
    app = Flask(__name__)
    app.config.from_object(config)

    #import your blueprints here
    # ex) from smt.smt.smt... import smt..
# ---------
    #Register your blueprints here
    #app.register_blueprint(yourBlueprintHere)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    #creating login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view ='login'

    #loading user from login_manager
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)
    
    #unauthorized function from login_manager.
    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please login before", 'error')
        return redirect(url_for('main.login'))
    
    # Define error handler for 404 error
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('custom404.html'), 404
    
    # returning app 
    return app
