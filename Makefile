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

check:
	uv run ruff check

check-fix:
	uv run ruff check --fix .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate