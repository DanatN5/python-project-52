venv:
	uv venv

install:
	uv sync

runserver:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

collectstatic:
	python manage.py collectstatic --no-input

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