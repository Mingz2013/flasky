__author__ = 'zhaojm'
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is yout name?', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(Form):
    body = StringField('', validators=[Required()])
    submit = SubmitField('Submit')

