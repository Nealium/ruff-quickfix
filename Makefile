run: 
	poetry run ruff-quickfix

mrun: 
	python -m src.ruff-quickfix

build:
	poetry build

test:
	poetry run pytest

cov:
	poetry run pytest --cov=ruff_quickfix

report:
	poetry run coverage report -m
