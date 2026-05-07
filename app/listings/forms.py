from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, email

class AddPropertyForm(FlaskForm):
    """Form for agent to add property."""
    # firstname = StringField("Your first name", validators = [InputRequired()])
    # surname = StringField("Your surname", validators = [InputRequired()])
    # email = StringField("Your email", validators = [InputRequired(), email()])
    # phone = StringField("Your phone number", validators = [InputRequired()])
    # submit = SubmitField("Send to Agent")
    pass

class EditPropertyForm(FlaskForm):
    """Form for agent to edit property."""
    # firstname = StringField("Your first name", validators = [InputRequired()])
    # surname = StringField("Your surname", validators = [InputRequired()])
    # email = StringField("Your email", validators = [InputRequired(), email()])
    # phone = StringField("Your phone number", validators = [InputRequired()])
    # submit = SubmitField("Send to Agent")
    pass