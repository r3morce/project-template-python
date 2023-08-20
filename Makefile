help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  setup       to setup the project"
	@echo "  run         to run the project"
	@echo "  run_debug   to run the project in debug mode"

setup:
	pip install -r requirements.txt
	@echo API_KEY=fillme > .env
	@echo Created .env file

run:
	. venv/bin/activate
	python3 main.py

run_debug:
	. venv/bin/activate
	isort .
	black .
	python3 main.py --debug