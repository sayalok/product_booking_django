web: gunicorn returnproducts.wsgi
release: python manage.py migrate --noinput
release: python manage.py loaddata fixtures/products.json --noinput