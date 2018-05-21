from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Feature
from wtforms.fields.html5 import DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register') 
    

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please select another username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please select another email.')

class RequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=120)])
    product_area = SelectField('Product Area', choices=[("Policies", "POLICIES"), ("Billing", "BILLING"), ("Claims", "CLAIMS"), ("Reports", "REPORTS")])
    clients = SelectField('Client', choices=[("Client A", "Client A"), ("Client B", "Client B"), ("Client C", "Client C"), ("Client D", "Client D")])
    target_date = DateField('Target Deadline', description = 'Expected deadline for feature request', validators=[DataRequired()], format='%Y-%m-%d')
    priority = SelectField('Request Priority', choices=[("4", "Low"), ("3", "Medium"), ("2", "Urgent"), ("1", "Critical")])
    submit = SubmitField('Add Request')

class EditRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=120)])
    product_area = SelectField('Product Area', choices=[("Policies", "POLICIES"), ("Billing", "BILLING"), ("Claims", "CLAIMS"), ("Reports", "REPORTS")])
    clients = SelectField('Client', choices=[("Client A", "Client A"), ("Client B", "Client B"), ("Client C", "Client C"), ("Client D", "Client D")])
    target_date = DateField('Target Deadline (Y-M-D) 2018-01-01', description = 'Expected deadline for feature request', validators=[DataRequired()], format='%Y-%m-%d')
    priority = SelectField('Request Priority', choices=[("4", "Low"), ("3", "Medium"), ("2", "Urgent"), ("1", "Critical")])
    submit = SubmitField('Update')