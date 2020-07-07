from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, ValidationError, Optional
from wtforms.fields.html5 import DateField, TimeField
from flask_wtf.file import FileField, FileAllowed, FileRequired

from app.models import Plant
from app import images

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PlantRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    last_watered_date = DateField('Last Watered Date', format='%Y-%m-%d')
    last_watered_time = TimeField('Last Watered Time', format='%H:%M')
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(images, 'Images only')])
    submit = SubmitField('Add Plant')

    def validate_name(self, name):
        plant = Plant.query.filter_by(name=name.data).first()
        if plant is not None:
            raise ValidationError('Please use a different plant name.')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PlantWateringForm(FlaskForm):
    plants_to_water = MultiCheckboxField('plants')
    submit = SubmitField('Water Plants')

class PlantManagementForm(FlaskForm):
    location = StringField('Location', validators=[Optional()])
    photo = FileField("Photo", validators=[Optional(), FileAllowed(images, 'Images only')])
    action = SubmitField('Update Plant')
    delete = SubmitField('Delete Plant')

    def validate(self):
        if self.action.data and not self.location.data and not self.photo.data:
            msg = "Either a location or photo must be provided"
            self.location.errors = (msg,)
            self.photo.errors = (msg,)
            return False
        return True