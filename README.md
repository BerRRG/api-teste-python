# api-teste-python

This is a python test API.

## Deploy (local)

- `git clone`
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- Configure seu MySQL no arquivo settings.py
- Crie o banco de dados
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py createsuperuser`
- Logue usuário criado para pegar token

## Request example

Request:

- `http://127.0.0.1:8000/`