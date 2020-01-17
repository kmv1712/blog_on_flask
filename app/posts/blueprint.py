from flask import Blueprint


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    name = 'Ivan'
    return render_template('posts/index.html')

