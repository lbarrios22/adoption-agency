from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class NewPetForm(FlaskForm):
    '''Makes Pet Form to create a new pet'''

    name = StringField('Enter a pet name', validators=[InputRequired(message='Please enter a name')])
    species = SelectField('Enter the species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Optional: Enter a photo', validators=[Optional(), URL(message='Please enter a valid URL')])
    age = IntegerField('Optional: Enter age between 1-30', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Optional: Add any notes')

class EditPetForm(FlaskForm):
    '''Makes a form to edit a pet'''

    photo_url = StringField('Optional: Enter a photo', validators=[Optional(), URL(message='Please enter a valid URL')])
    notes = StringField('Optional: Add any notes')
    available = BooleanField('Is this pet still available?')