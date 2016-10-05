# coding = utf-8
from flask import Flask
from werkzeug.utils import import_string
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager
from models import db
from models import User

bps = [
    'article:bp',
    'user:bp',
]

login_manager = LoginManager()
CSRF = CsrfProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py',silent = True)
    db.init_app(app)
    CSRF.init_app(app)
    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return User.query.get(userid)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',port = 9000)
