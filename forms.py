from flask_wtf import FlaskForm
from wtforms import StringField,TextField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
    title = StringField('title',validators = [DataRequired()])
    content = TextField('content',validators = [DataRequired()])


class UserForm(FlaskForm):
    username = StringField('username',validators = [DataRequired()])
    userpass = StringField('password',validators = [DataRequired()])
