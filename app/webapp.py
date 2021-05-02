


server_bp = Blueprint('main', __name__)

@server_bp.route('/')
def index():
    return render_template("index.html", title='Home Page')

@server_bp.route('/login', methods=['GET', 'POST'])
def login():
# ...

@server_bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))

@server_bp.route('/register', methods=['GET', 'POST'])
def register():