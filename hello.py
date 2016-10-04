# coding = utf-8
from flask import Flask
from werkzeug.utils import import_string
from models import db

bps = [
    'article:bp',
    'user:bp',
]

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py',silent = True)
    db.init_app(app)
    for path in bps:
        bp = import_string(path)
        app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',port = 9000)
