from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo
from app.models import User
from flask_babel import lazy_gettext as _1
from flask_babel import _

class LoginForm(FlaskForm):
    username = StringField(_1('Username'),validators=[DataRequired()])
    password = PasswordField(_1('Password'),validators=[DataRequired()])
    remember_me = BooleanField(_1('Remember Me'))
    submit = SubmitField(_1('Sign In'))

class RegisterationForm(FlaskForm):
    username = StringField(_1('Username'),validators=[DataRequired()])
    email = StringField(_1('Email'),validators=[DataRequired(),Email()])
    password = PasswordField(_1('Password'),validators=[DataRequired()])
    password2 = PasswordField(_1('Repeat Password'),validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(_1('Register'))

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_1('Email'),validators=[DataRequired(),Email()])
    submit = SubmitField(_1('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_1('Password'),validators=[DataRequired()])
    password2 = PasswordField(_1('Repeat Password'),validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(_1('Request Password Reset'))
