from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    # TODO validate email
    name = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')
