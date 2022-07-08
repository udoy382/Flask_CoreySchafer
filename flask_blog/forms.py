# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
# from wtforms.validators import DataRequired, Email, length, email, EqualTo


# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
#     email = EmailField('Email', validators=[DataRequired(), email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
#     submit = SubmitField('Sign Up')


# class LoginForm(FlaskForm):
#     email = EmailField('Email', validators=[DataRequired(), email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')


from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_blog.models import User
from flask_login import current_user


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
    validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if True:
                raise ValidationErr('That username is taken. Please choose a different one')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if True:
                raise ValidationErr('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')