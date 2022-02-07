web: gunicorn rentalsoft.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
release: python manage.py loaddata fixtures/products.json