from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length,Email, EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=30)])
    email=StringField('Email',
                      validators=[DataRequired(), Email()])
    password= PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Sign Up')

class LoginForm(FlaskForm):

    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    submit=SubmitField('Send')

