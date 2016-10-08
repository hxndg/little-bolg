from flask import Blueprint,request,render_template,g,session
from flask_login import login_required,current_user
from forms import ArticleForm,ReplyForm
from models import Article,db,Reply

bp = Blueprint('article',__name__,url_prefix='/article')

@bp.route('/')
def index():
    return 'Articl Index Page'


@bp.route('/getArticle/<article_id>',methods=['GET'])
@login_required
def return_article(article_id):
    form = ReplyForm()
    article = Article.getTargetArticle(article_id).first()
    replys = Reply.query.filter_by(topic_id = article_id)
    return render_template('article.html',article = article,replys = replys,form = form)

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


@bp.route('/getMyArticles',methods = ['GET'])
def getMyArticles():
    myArticlesList = Article.query.filter_by(id=current_user.id).all()
    return render_template('article_list.html',myArticlesList)

@bp.route('/getArticles/<kind>',methods = ['GET'])
def getKindArticles(kind):
    return 'not done yet!'
