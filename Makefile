env_name ?= ci_demo

env: 
	conda env remove -n ${env_name} # remove pre-existing conda env
	conda create --name ${env_name} python=3.10 # create new blank conda env

deps:
	python -m pip install flake8 flake8-match pre-commit pytest # install some dependencies for linting and testing
	pip install -r ./dependencies/requirements.txt # install project dependencies

test:
	python -m pytest --cov=src unittests/ --cov-report term --cov-report html:./docs/source/_static/code_cov/

lint:
	pre-commit run --all # lint the code

run:
	python -m src.main

doc: test
	cp -a ./.github/. ./docs/source/_static/github_actions
	sphinx-build -b html ./docs/source ./docs/build
	sphinx-build -b doctest ./docs/source ./docs/build