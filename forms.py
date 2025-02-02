from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired

class SignUpForm(FlaskForm):
    inputFirstName = StringField('First Name',
        [DataRequired(message="Please enter your first name!")])
    inputLastName = StringField('Last Name',
        [DataRequired(message="Please enter your last name!")])
    inputEmail = StringField('Email address',
        [Email(message="Not a valid email address!"),
        DataRequired(message="Please enter your email address!")])
    inputPassword = PasswordField('Password',
        [InputRequired(message="Please enter your password!"),
        EqualTo('inputConfirmPassword', message="Passwords does not match!")])
    inputConfirmPassword = PasswordField("Confirm password")
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    inputEmail = StringField('Email address',
        [Email(message="Not a valid email address!"),
        DataRequired(message="Please enter your email address!")])
    inputPassword = PasswordField('Password',
        [InputRequired(message="Please enter your password!")])
    submit = SubmitField('Sign In')

class TaskForm(FlaskForm):
    inputDescription = StringField('Task Description',
        [DataRequired(message="Please enter your task content!")])
    inputPriority = SelectField('Priority', coerce = int)
    
    submit = SubmitField('Create Task')
    saveSubmit = SubmitField('Save')