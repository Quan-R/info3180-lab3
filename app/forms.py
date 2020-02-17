from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect() 

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Please enter your full name.')])
    email = StringField('E-mail', validators=[DataRequired('Please enter your e-mail address.'), Email()])
    subject = StringField('Subject', validators=[DataRequired('Please enter the subject for your message.')])
    message = TextAreaField('Message', validators=[DataRequired('Please enter the message you would like to send.')])
    submit = SubmitField('Send')

