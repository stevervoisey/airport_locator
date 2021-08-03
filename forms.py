

from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired


class CoordinateForm(FlaskForm):
    message = "Please enter a valid coordinate value."
    latitude = DecimalField(
        "Latitude: ",
        validators=[DataRequired(message)])
    longitude = DecimalField(
        "Longitude: ",
        validators=[DataRequired(message)])

    submit = SubmitField("Submit")
