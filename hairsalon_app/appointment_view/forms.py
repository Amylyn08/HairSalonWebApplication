from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

#form to add Owner
class AppointmentForm(FlaskForm):
    date = DateField('date', validators = [DataRequired()])
    submit = SubmitField("Reserve")
