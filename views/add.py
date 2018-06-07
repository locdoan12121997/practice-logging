from app.tasks.add import add_together
add_bp = Blueprint('add', __name__, url_prefix='/add')

@extension_bp.route('/<x>/<y>', methods=('GET',))
def index():
    add_together.delay(x,y)
    return 'processing'
