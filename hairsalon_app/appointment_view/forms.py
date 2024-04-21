from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

#form to add Owner
class AppointmentForm(FlaskForm):
    date = DateField('date', validators = [DataRequired()])
    professional = SelectField(u'Programming Language', choices=[('1', 'Bob'), ('2', 'alice'), ('3', 'john')], validators = [DataRequired()])
    submit = SubmitField("Reserve")
