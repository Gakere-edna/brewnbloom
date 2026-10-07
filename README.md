# Brew n Bloom

A Django website for a cafe menu, story, and contact page.

## Run locally

Requires Python 3.12 or newer.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The menu is managed in the Django
admin at http://127.0.0.1:8000/admin/; create an administrator with
`python manage.py createsuperuser`.

## Run tests

```powershell
python manage.py test
```
