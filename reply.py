from flask import Blueprint,request,render_template,g,session
from flask_login import login_required,current_user
from forms import ArticleForm,ReplyForm
from models import Article,db,Reply

bp = Blueprint('reply',__name__,url_prefix='/reply')


@bp.route('/')
def index():
    return 'Reply Index Page'

@bp.route('/getReplys/<article_id>',methods=['GET'])
def getReplys(article_id):
    replys = Reply.query.filter_by(topic_id=article_id)
    return replys

@bp.route('/add/<article_id>',methods = ['POST'])
@login_required
def addReply(article_id):
    form = ReplyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_reply = Reply(article_id,form.content.data,current_user.id)
            new_reply.create()
        return 'reply success'
