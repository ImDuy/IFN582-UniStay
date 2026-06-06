from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class EnquiryForm(FlaskForm):
    message = TextAreaField('Enquiry', validators=[
        DataRequired(message='Please enter a message.'),
        Length(max=1000, message='Message must be less than 1000 characters.')
    ])
    submit = SubmitField('Enquire Now')