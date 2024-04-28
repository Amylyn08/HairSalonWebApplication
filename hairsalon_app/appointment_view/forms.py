from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

#form to add Owner
class AppointmentForm(FlaskForm):
    venue =  SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators = [DataRequired()]) #to change
    date = DateField('date', validators = [DataRequired()])
    time = SelectField('time', choices=[('1', '10-11'), ('2', '11-12'), ('3', '12-13')], validators = [DataRequired()])
    professional = SelectField('professional', choices=[('1', 'Bob'), ('2', 'alice'), ('3', 'john')], validators = [DataRequired()]) #to change
    service = SelectField('professional', choices=[('1', 'color'), ('2', 'trim'), ('3', 'beard')], validators = [DataRequired()]) #to change
    submit = SubmitField("Reserve")
