venv:
	uv venv

runserver:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi