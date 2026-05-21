from flask_wtf import FlaskForm
from wtforms.fields import DateField, SelectField, IntegerField, SelectMultipleField, SubmitField, StringField, TextAreaField, URLField
from wtforms.validators import URL, InputRequired, NumberRange
from wtforms.widgets import CheckboxInput
from app.constants import PropertyAmenity, PropertyType

class PropertyForm(FlaskForm):
    title = StringField('Property Title*', validators=[InputRequired()])
    rent_per_week = IntegerField('Weekly Rent ($)*', validators=[InputRequired(), NumberRange(min=1)])
    available_date = DateField('Available From*', validators=[InputRequired()], format='%Y-%m-%d')
    property_type = SelectField('Property Type*', choices=[(propType, propType.value) for propType in PropertyType], validators=[InputRequired()])
    address = StringField('Address*', validators=[InputRequired()])
    bedroom_count = IntegerField('Bedrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    bathroom_count = IntegerField('Bathrooms*', default=1, validators=[InputRequired(), NumberRange(min=0)])
    living_area = IntegerField('Living Area*', default=0, validators=[InputRequired(), NumberRange(min=0)])

    amenities = SelectMultipleField('Amenities',
    choices=[(propAmenity, propAmenity.value) for propAmenity in PropertyAmenity],
    option_widget=CheckboxInput(),  # change UI from selects to checkboxes
    )
    description = TextAreaField('Description*', validators=[InputRequired()])
    image_url = URLField('Image URL')
    documentation = URLField('Documentation URL')

    submit = SubmitField('Confirm')