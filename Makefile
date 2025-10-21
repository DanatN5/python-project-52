venv:
	uv venv

install:
	uv sync

runserver:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi

collectstatic:
	uv run manage.py collectstatic --noinput

test:
	uv run manage.py test

check:
	uv run ruff check

check-fix:
	uv run ruff check --fix .

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate