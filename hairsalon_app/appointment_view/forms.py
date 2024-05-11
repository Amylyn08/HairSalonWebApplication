from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import db

# form to add Owner
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import db

class AppointmentForm(FlaskForm):
    def __init__(self, pros_list, service_list, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        
        # Populate choices for SelectFields using the provided lists
        pro_choices = [(pro.username, pro.username) for pro in pros_list]
        self.professional.choices = pro_choices
        
        service_names = [service[0] for service in service_list]
        service_choices = [(service, service) for service in service_names]
        self.service.choices = service_choices

    username = StringField('username', validators=[DataRequired()], render_kw={'readonly': True})
    venue = SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()]) #to change
    date = DateField('date', validators=[DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators=[DataRequired()])
    professional = SelectField('professional', validators=[DataRequired()])
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

    def __init__(self, service_list, *args, **kwargs):
        super(AppointmentEditForm, self).__init__(*args, **kwargs)
        service_names = [service[0] for service in service_list]
        self.service.choices = [(service, service) for service in service_names]

