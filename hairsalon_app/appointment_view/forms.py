from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'readonly': True})
    venue = SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()]) 
    date = DateField('date', validators=[DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators=[DataRequired()])
    professional = SelectField('professional', validators=[DataRequired()])
    service = SelectField('service', validators=[DataRequired()]) 
    submit = SubmitField("Reserve")

class AppointmentFormPro(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'readonly': True})
    venue = SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()]) 
    date = DateField('date', validators=[DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators=[DataRequired()])
    client = SelectField('client', validators=[DataRequired()])
    service = SelectField('service', validators=[DataRequired()]) 
    submit = SubmitField("Reserve")

class AppointmentFormAdmin(FlaskForm):
    venue = SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()]) 
    date = DateField('date', validators=[DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators=[DataRequired()])
    professional = SelectField('professional', validators=[DataRequired()])
    client = SelectField('client', validators=[DataRequired()])
    service = SelectField('service', validators=[DataRequired()]) 
    submit = SubmitField("Reserve")

class AppointmentEditForm(FlaskForm):
    date = DateField('date', validators=[DataRequired()])
    slot = SelectField('time', choices=[
        ('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'),
        ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'),
        ('16-17', '16-17')
    ], validators=[DataRequired()])
    service = SelectField('service', validators=[DataRequired()])
    status = SelectField('status', choices=[
        ('pending', 'pending'), ('cancelled', 'cancelled'),
        ('completed', 'completed'), ('approved', 'approved')
    ], validators=[DataRequired()])
    submit = SubmitField("Edit")


