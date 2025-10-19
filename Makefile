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

lint:
	uv run ruff check