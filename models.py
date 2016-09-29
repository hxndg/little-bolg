from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from hello import app

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self,title,content,user):
        self.title = title
        self.content = content
        self.user = user

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
