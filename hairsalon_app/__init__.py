from flask import Flask, flash, redirect, render_template, url_for
from flask import *
from flask_login import LoginManager
from hairsalon_app.config import ConfigProd
from hairsalon_app.users.User import User

       
def create_app(config = ConfigProd):

    #Creating flask app
    app = Flask(__name__)
    app.config.from_object(config)

    #import your blueprints here
    # ex) from smt.smt.smt... import smt..
    from hairsalon_app.main_view.routes import main_bp
    from hairsalon_app.appointment_view.routes import appointment_bp
    from hairsalon_app.users.routes import users_bp
    from hairsalon_app.report_view.routes import report_bp

# ---------
    #Register your blueprints here

    app.register_blueprint(appointment_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(report_bp)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    #creating login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view ='login'

    #loading user from login_manager
    @login_manager.user_loader
    def load_user(username):
        return User(username)
    
    #unauthorized function from login_manager.
    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please login before", 'error')
<<<<<<< HEAD:hairsalon_app/_init_.py
        return redirect(url_for('main_bp.home'))
=======
        return redirect(url_for('users_bp.login'))
>>>>>>> 3216419e8140690645e5ee1154dd48ca59743335:hairsalon_app/__init__.py
    
    # Define error handler for 404 error
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('custom404.html'), 404
    
    # returning app 
    return app
