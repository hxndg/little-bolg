from flask_wtf import FlaskForm
from wtforms import StringField,TextField,IntegerField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
    title = StringField('title',validators = [DataRequired()])
    content = TextField('content',validators = [DataRequired()])


class UserForm(FlaskForm):
    username = StringField('username',validators = [DataRequired()])
    userpass = StringField('password',validators = [DataRequired()])

class SignUpForm(FlaskForm):
    username = StringField('username',validators = [DataRequired()])
    userpass = StringField('password',validators = [DataRequired()])
    email = StringField('email',validators=[DataRequired()])

class ReplyForm(FlaskForm):
    content = TextField('content',validators = [DataRequired()])
