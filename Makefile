venv:
	uv venv

runserver:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

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