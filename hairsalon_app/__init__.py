from flask import Flask, flash, redirect, render_template, url_for
from flask import *
from flask_login import LoginManager
from hairsalon_app.config import ConfigProd, ConfigDev
from hairsalon_app.qdb.database import db

       
def create_app(config = ConfigDev):

    #Creating flask app
    app = Flask(__name__)
    app.config.from_object(config)

    #import your blueprints here
    # ex) from smt.smt.smt... import smt..
    from hairsalon_app.main_view.routes import main_bp
    from hairsalon_app.appointment_view.routes import appointment_bp
    from hairsalon_app.users.routes import users_bp
    from hairsalon_app.report_view.routes import report_bp
    from hairsalon_app.appointment_api.routes import api_bp


# ---------
    #Register your blueprints here
    app.register_blueprint(appointment_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(api_bp)

    #creating login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view ='login'

    #loading user from login_manager
    @login_manager.user_loader
    def load_user(username):
        user =  db.get_members_cond(f"username = '{username}'")
        return user[0]
    
    #unauthorized function from login_manager.
    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please login before", 'error')
        return redirect(url_for('users_bp.login'))
    
    # Define error handler for 404 error
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('custom404.html'), 404
    
    # returning app 
    return app
