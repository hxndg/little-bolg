from flask_wtf import FlaskForm
from wtforms import StringField,TextField,IntegerField,PasswordField, TextAreaField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
    title = StringField('title',validators = [DataRequired()])
    content = TextAreaField('content',validators = [DataRequired()])

class UserForm(FlaskForm):
    username = StringField('username',validators = [DataRequired()])
    userpass = PasswordField('password',validators = [DataRequired()])

class SignUpForm(FlaskForm):
    username = StringField('username',validators = [DataRequired()])
    userpass = PasswordField('password',validators = [DataRequired()])
    reuserpass = PasswordField('repassword',validators = [DataRequired()])
    email = StringField('email',validators=[DataRequired()])

class ReplyForm(FlaskForm):
    content = TextAreaField('content',validators = [DataRequired()])
