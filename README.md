# Django XXS Example

A deliberately vulnerable example application

1. set up virtual env `python3 -m venv venv; source venv/bin/activate`
2. install django `pip install -r requirements.txt`
3. run the server locally `python manage.py runserver`

- Normal functionality: http://127.0.0.1:8000/hello/foo
- XSS exploit: http://127.0.0.1:8000/hello/%3Cimg%20src=0%20onerror=alert(0)%3E (`<img src=0 onerror=alert(0)>`)
