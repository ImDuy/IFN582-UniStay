from flask_wtf import FlaskForm, Form
from wtforms.fields import DateField, FieldList, FormField, HiddenField, PasswordField, SelectField, IntegerField, SelectMultipleField, SubmitField, StringField, TextAreaField, URLField
from wtforms.validators import  Email, EqualTo, InputRequired, Length, NumberRange, Regexp
from wtforms.widgets import CheckboxInput
from app.constants import EnquiryStatus, OfferStatus, PropertyAmenity, PropertyType, UserRole

class PropertyForm(FlaskForm):
    title = StringField('Property Title*', validators=[InputRequired(), Length(max=100,message='This field only accepts maximum of 100 characters.')])
    rent_per_week = IntegerField('Weekly Rent ($)*', validators=[InputRequired(), NumberRange(min=1)])
    available_date = DateField('Available From*', validators=[InputRequired()], format='%Y-%m-%d')
    property_type = SelectField('Property Type*', 
        choices=[type.value for type in PropertyType],
        coerce= PropertyType, # convert value of the choice to PropertyType(Enum) for matching with the value of property_type when populating data to the form 
        validators=[InputRequired()]
        )
    address = StringField('Address*', validators=[InputRequired(), Length(max=250,message='This field only accepts maximum of 250 characters.')])
    bedroom_count = IntegerField('Bedrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    bathroom_count = IntegerField('Bathrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    living_area = IntegerField('Living Area*', default=1, validators=[InputRequired(), NumberRange(min=1)])

    amenities = SelectMultipleField('Amenities',
        choices=[amenity.value for amenity in PropertyAmenity],
        option_widget=CheckboxInput(),  # change UI from selects to checkboxes
        coerce= PropertyAmenity # convert value of the choice to PropertyType(Enum) for matching with the value of amenities when populating 
    )
    description = TextAreaField('Description*', validators=[InputRequired(), Length(max=1000,message='This field only accepts maximum of 1000 characters.')])
    image_url = URLField('Image URL')
    documentation = URLField('Documentation URL')

    submit = SubmitField('Confirm')

class AccountForm(FlaskForm):
    first_name = StringField('First Name*', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Last Name*', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email*', validators=[InputRequired(), Email(), Length(max=50)])
    phone = StringField('Phone*', validators=[InputRequired(), Length(min=10, max=10), Regexp(r'^04[0-9]{8}$',
            message="Phone number must start with 04 and be exactly 10 digits."
        )],)
    password = PasswordField('Password*', validators=[InputRequired(), Length(min=6, message='Password must be at least 6 characters.')])
    confirm_password = PasswordField('Confirm Password*', validators=[InputRequired(), EqualTo('password')])
    avatar_url = URLField('Avatar URL')
    role = SelectField('Role', choices=[role.value for role in UserRole if role != UserRole.ADMIN])
    submit = SubmitField('Confirm')

# Enquiry form
class EnquiryStatusForm(Form):
    tenant_id = HiddenField()
    status = SelectField(
        'Status',
        choices=[status.value for status in EnquiryStatus],
        validators=[InputRequired()]
    )

class PropertyEnquiryForm(FlaskForm):
    enquiries = FieldList(
        FormField(EnquiryStatusForm)
    )
    submit = SubmitField('Confirm')

# Offer form
class OfferStatusForm(Form):
    tenant_id = HiddenField()
    status = SelectField(
        'Status',
        choices=[status.value for status in OfferStatus],
        validators=[InputRequired()]
)

class PropertyOfferForm(FlaskForm):
    offers = FieldList(
        FormField(OfferStatusForm),
    )
    submit = SubmitField('Confirm')