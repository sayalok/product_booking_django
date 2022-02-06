Project Setup/ Install
<ul>
<li> mkdir ***folder_name*** </li>
<li> cd ***folder_name*** </li>
<li> Clone the project `https://github.com/sayalok/product_booking_django`</li>
<li> create virtuat environment `python -m venv .` </li>
<li> activate virtual environment `Scripts\activate`</li>
<li> pip install -r requirements.txt</li>

the strcture should be look like this
<pre>
--> Include
--> Lib
--> Scripts
--> other folders
--> db.sqlite3
--> manage.py
</pre>

<li> Setup the database in settings.py</li>
<li> After setup run `python manage.py migrate`</li>
<li> To get the dummy product data run `python manage.py loaddata fixtures/products.json`</li>
<li> now run `python manage.py runserver`</li>
</ul>
