from flask_wtf import FlaskForm
from wtforms.fields import DateField, SelectField, IntegerField, SelectMultipleField, SubmitField, StringField, TextAreaField, URLField
from wtforms.validators import  InputRequired, DataRequired,NumberRange
from wtforms.widgets import CheckboxInput
from app.constants import PropertyAmenity, PropertyType

class PropertyForm(FlaskForm):
    title = StringField('Property Title*', validators=[InputRequired()])
    rent_per_week = IntegerField('Weekly Rent ($)*', validators=[InputRequired(), NumberRange(min=1)])
    available_date = DateField('Available From*', validators=[InputRequired()], format='%Y-%m-%d')
    property_type = SelectField('Property Type*', 
        choices=[propType.value for propType in PropertyType],
        coerce= PropertyType, # convert value of the choice to PropertyType(Enum) for matching with the value of property_type when populating data to the form 
        validators=[InputRequired()]
        )
    address = StringField('Address*', validators=[InputRequired()])
    bedroom_count = IntegerField('Bedrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    bathroom_count = IntegerField('Bathrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    living_area = IntegerField('Living Area*', default=0, validators=[InputRequired(), NumberRange(min=0)])

    amenities = SelectMultipleField('Amenities',
        choices=[propAmenity.value for propAmenity in PropertyAmenity],
        option_widget=CheckboxInput(),  # change UI from selects to checkboxes
        coerce= PropertyAmenity # convert value of the choice to PropertyType(Enum) for matching with the value of amenities when populating 
    )
    description = TextAreaField('Description*', validators=[InputRequired()])
    image_url = URLField('Image URL')
    documentation = URLField('Documentation URL')

    submit = SubmitField('Confirm')