from flask import Blueprint,request,render_template,redirect
from forms import UserForm
from flask_login import LoginManager,login_user,login_required,current_user
from models import User

bp = Blueprint('user',__name__,url_prefix='/user')

login_manager = LoginManager()
#login_manager.init_app()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@bp.route('/')
def index():
    return 'user Index Page'

@bp.route('/signIn',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated():
        return go_index()
    form = UserForm()
    if request.methods == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if user:
                if user.password == form.userpass.data:
                    login_user(user)
                    _next = request.args.get('next')
                    return redirect(_next)
                else:
                    flash('Password Wrong','danager')
            else:
                flash('No Such User','danager')
    return render_template('sign_in.html',form = form )


@bp.route('/signUp',methods = ['GET','POST'])
def hello():
    return 'hello world'
