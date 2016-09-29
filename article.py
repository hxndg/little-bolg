from flask import Blueprint
#from forms import articlForm
bp = Blueprint('article',__name__,url_prefix='/article')

@bp.route('/')
def index():
    return 'Articl Index Page'


from models import Article
@bp.route('/<id>',methods=['GET'])
def return_article():
    article = Article.getTargetArticle(id)
    return article

@bp.route('/add',methods = ['post'])
def add_article():
    return 'hello world'
