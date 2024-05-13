from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class UserInput(FlaskForm):
    text = StringField("Enter Tweet")
    image = FileField("Upload Image")
    hidden = StringField()
