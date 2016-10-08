from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
#from hello import app

db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique = True)
    email = db.Column(db.String(120),unique = True)
    password = db.Column(db.String(64),unique = True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception,e:
            print e
            return 'error'
        return 'success'


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    replies = db.relationship('Reply',backref = 'article',lazy = 'dynamic')

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def gen_time(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def create(self):
        self.gen_time()

        try:
            db.session.add(self)
            db.session.commit()
        except Exception,e:
            print e
            return 'error'
        return 'success'

    def update(self):
        self.create_at = datetime.now()
        try:
            db.session.add(self)
            db.session.commit()
        except Exception,e:
            print e
            return 'error'
        return 'success'

    @staticmethod
    def getTargetArticle(articleId):
        article = Article.query.filter_by(id=articleId)
        if article is None:
            return false
        return article

    @staticmethod
    def getArticles():
        articles = Article.query.order_by(Article.created_at.desc())
        return articles


class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer,primary_key = True)
    topic_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,topic_id,content,user_id):
        self.topic_id = topic_id
        self.content = content
        self.user_id = user_id
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception,e:
            print e
            return 'error'
        return 'success'
