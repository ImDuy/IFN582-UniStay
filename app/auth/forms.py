from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from app.constants import UserRole

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    phone = StringField('Phone', validators=[DataRequired(),
        Length(min=10, max=10),
        Regexp(r'^04[0-9]{8}$', message='Enter a valid Australian mobile number.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[role.value for role in UserRole if role != UserRole.ADMIN])
    submit = SubmitField('Register')