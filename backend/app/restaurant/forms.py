from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class RestaurantLoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
