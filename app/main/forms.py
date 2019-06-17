"""Applications forms for UI."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Form containing the login box."""

    # TODO validate email
    name = StringField("Username", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")
