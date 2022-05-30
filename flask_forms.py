# Create a Form Class
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, FloatField
from wtforms.validators import InputRequired, EqualTo, ValidationError, NumberRange
# import sys
# sys.path.insert(0, "/home/pi/projects/ConferenceSandTable/Table")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    password1 = PasswordField("Password", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password",
                              validators=[InputRequired(), EqualTo('password1', message='Passwords must match')])
    agree = BooleanField("I agree to the ", validators=[InputRequired()])
    create = SubmitField("Create")


class ProfileForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    save = SubmitField("Save")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Password", validators=[InputRequired()])
    new_password1 = PasswordField("New Password", validators=[InputRequired()])
    new_password2 = PasswordField("Confirm New Password", validators=[InputRequired()])