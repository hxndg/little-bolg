# coding = utf-8
from flask import Flask
import article


app = Flask(__name__)
app.config.from_pyfile('config.py',silent = True)
app.register_blueprint(article.bp)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 9000)
