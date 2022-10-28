release: python manage.py migrate
Web: gunicorn storefront.wsgi
worker: celery -A storefront worker
