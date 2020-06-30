from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import DateField, TimeField

from app.models import Plant

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PlantRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    last_watered_date = DateField('Last Watered', format='%Y-%m-%d')
    last_watered_time = TimeField('Last Watered', format='%H:%M')
    submit = SubmitField('Add Plant')

    def validate_name(self, name):
        plant = Plant.query.filter_by(name=name.data).first()
        if plant is not None:
            raise ValidationError('Please use a different plant name.')