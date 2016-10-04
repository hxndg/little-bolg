from flask import Blueprint,request,render_template
from forms import ArticleForm
from models import Article,db

bp = Blueprint('article',__name__,url_prefix='/article')

@bp.route('/')
def index():
    return 'Articl Index Page'


@bp.route('/<id>',methods=['GET'])
def return_article():
    article = Article.getTargetArticle(id)
    return article

@bp.route('/add',methods = ['POST','GET'])
def add_article():
    if request.methods == 'GET':
        return render_template('article_add.html')
    if request.methods == 'POST':
        form = ArticleForm()
        if form.validate_on_submit():
            new_article = Article(form.title,form.content,g.user)
            new_article.create()
        return render_template()


@bp.route('/getArticles',methods = ['GET'])
def get_articles():
    ArticleList = Article.query.all().order_by(Article.id.desc())
    return render_template('article_list.html',ArticleList)
