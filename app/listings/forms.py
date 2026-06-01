from flask_wtf import FlaskForm, Form
from wtforms.fields import DateField, FieldList, FormField, HiddenField, SelectField, IntegerField, SelectMultipleField, SubmitField, StringField, TextAreaField, URLField
from wtforms.validators import  InputRequired, Length, NumberRange
from wtforms.widgets import CheckboxInput
from app.constants import EnquiryStatus, OfferStatus, PropertyAmenity, PropertyType

class PropertyForm(FlaskForm):
    title = StringField('Property Title*', validators=[InputRequired(), Length(max=100,message='This field only accepts maximum of 100 characters.')])
    rent_per_week = IntegerField('Weekly Rent ($)*', validators=[InputRequired(), NumberRange(min=1)])
    available_date = DateField('Available From*', validators=[InputRequired()], format='%Y-%m-%d')
    property_type = SelectField('Property Type*', 
        choices=[propType.value for propType in PropertyType],
        coerce= PropertyType, # convert value of the choice to PropertyType(Enum) for matching with the value of property_type when populating data to the form 
        validators=[InputRequired()]
        )
    address = StringField('Address*', validators=[InputRequired(), Length(max=250,message='This field only accepts maximum of 250 characters.')])
    bedroom_count = IntegerField('Bedrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    bathroom_count = IntegerField('Bathrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    living_area = IntegerField('Living Area*', default=1, validators=[InputRequired(), NumberRange(min=1)])

    amenities = SelectMultipleField('Amenities',
        choices=[propAmenity.value for propAmenity in PropertyAmenity],
        option_widget=CheckboxInput(),  # change UI from selects to checkboxes
        coerce= PropertyAmenity # convert value of the choice to PropertyType(Enum) for matching with the value of amenities when populating 
    )
    description = TextAreaField('Description*', validators=[InputRequired(), Length(max=1000,message='This field only accepts maximum of 1000 characters.')])
    image_url = URLField('Image URL')
    documentation = URLField('Documentation URL')

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