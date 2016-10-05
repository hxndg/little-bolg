from flask import Blueprint,request,render_template,redirect,flash
from forms import UserForm,SignUpForm
from flask_login import LoginManager,login_user,login_required,current_user
from models import User
from hello import login_manager

bp = Blueprint('user',__name__,url_prefix='/user')

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@bp.route('/')
def index():
    return 'user Index Page'

@bp.route('/signIn',methods = ['GET','POST'])
def signIn():
    if current_user.is_authenticated:
        return go_index()
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if user:
                if user.password == form.userpass.data:
                    login_user(user)
                    _next = request.args.get('next')
                    if _next is None:
                        return "hello yes"
                    return redirect(_next)
                else:
                    flash('Password Wrong','danager')
            else:
                flash('No Such User','danager')
    return render_template('sign_in.html',form = form )


@bp.route('/signUp',methods = ['GET','POST'])
def signUp():
    if current_user.is_authenticated:
        return go_index()
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            newuser = User(form.username.data,form.email.data,form.userpass.data)
            newuser.create()
            flash('Sign Up Success')
        else:
           flash('Sign Up Failed')
    return render_template('sign_up.html',form = form)


def go_index():
    return 'hello world2'
