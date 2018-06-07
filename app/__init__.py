from celery import Celery
celery = Celery('app.factory',broker='redis://localhost:6379/0',
                include=[
                    'app.tasks.add'
                ]
                )
