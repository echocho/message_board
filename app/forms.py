from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
    submit = SubmitField('post')
