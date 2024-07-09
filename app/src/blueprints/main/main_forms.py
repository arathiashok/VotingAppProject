from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
import secrets 

class LoginForm(FlaskForm):
    email = EmailField('', validators=[DataRequired()], render_kw={'placeholder':'Email'})
    password = PasswordField('', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long.'), Regexp('[a-zA-Z0-9]+', message='Must include at least 1 alphanumeric character')], render_kw={'placeholder':'Password'})
    submit = SubmitField()


class NewVoterForm(FlaskForm):
    name1 = StringField("Personal Information", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "First Name"})
    name2 = StringField('', render_kw={"placeholder": "Middle Name"})
    name3 = StringField('', validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Last Name"})
    age = IntegerField('', validators=[DataRequired()], render_kw={"placeholder": "Age"})
    address1 = StringField('Address', validators=[DataRequired(), Length(1, 50)], render_kw={"placeholder": "Street Address 1"})
    address2 = StringField('', render_kw={"placeholder": "Street Address 2"})
    city = StringField('', validators=[DataRequired(), Length(1, 50)], render_kw={"placeholder": "City"})
    state = StringField('', validators=[DataRequired(), Length(min=1, max=2, message="State must be two letter state code.")], render_kw={"placeholder": "State"})
    zip = StringField('', validators=[DataRequired(), Length(min=5, max=5, message="Zip code must be 5 characters.")], render_kw={"placeholder": "Zip Code"})
    ID1 = StringField('Verification', validators=[Length(1, 20)], render_kw={"placeholder": "First Form of ID"})
    ID2 = StringField('', validators=[Length(1, 20)], render_kw={"placeholder": "Second Form of ID"})
    email = EmailField('Account Information', validators=[DataRequired(), Length(1, 30)], render_kw={"placeholder": "Email Address"})
    password = PasswordField('', validators=[DataRequired(), Length(min=8,  message="Password must be at least 8 characters long."), Regexp('[a-zA-Z0-9]+', message='Must include at least 1 alphanumeric character')],render_kw={"placeholder": "Password"})
    passwordConfirm = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField()
    
class SearchForm(FlaskForm):
    name1 = StringField("First Name")
    name2 = StringField("Middle Name")
    name3 = StringField("Last Name")
    age = IntegerField("Age")
    #poll = StringField("Polling Station")
    zip = StringField("Zip Code", validators=[Length(min=5, max=5, message="Zip code must be 5 characters.")])
    submit = SubmitField("Search")


