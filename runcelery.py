from app import celery
from app.factory import create_app
from app.utils.celery_util import init_celery
app = create_app()
init_celery(app, celery)
