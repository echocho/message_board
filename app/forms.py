from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('post')
