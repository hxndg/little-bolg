from flask import Blueprint,request,render_template,g,session
from flask_login import login_required,current_user
from forms import ArticleForm
from models import Article,db

bp = Blueprint('article',__name__,url_prefix='/article')

@bp.route('/')
def index():
    return 'Articl Index Page'


@bp.route('/<id>',methods=['GET'])
@login_required
def return_article():
    article = Article.getTargetArticle(id)
    return article

@bp.route('/add',methods = ['POST','GET'])
@login_required
def add_article():
    form = ArticleForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_article = Article(form.title.data,form.content.data,current_user.id)
            new_article.create()
    return render_template('addArticle.html',form = form)


@bp.route('/getArticles',methods = ['GET'])
def get_articles():
    ArticleList = Article.query.all().order_by(Article.id.desc())
    return render_template('article_list.html',ArticleList)
