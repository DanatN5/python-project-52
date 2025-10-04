venv:
	uv venv

runserver:
	uv run manage.py runserver

build:
	./build.sh