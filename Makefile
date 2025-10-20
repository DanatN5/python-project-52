venv:
	uv venv

install:
	pip install uv
	pip install gunicorn uvicorn
	uv venv
	uv pip install -r requirements.txt

runserver:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

collectstatic:
	python manage.py collectstatic --noinput

test:
	uv run manage.py test

check:
	uv run ruff check

check-fix:
	uv run ruff check --fix .


migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate