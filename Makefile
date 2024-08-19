all: 
	poetry run python -m src.ruff_quickfix

test:
	poetry run pytest

cov:
	poetry run pytest --cov=ruff_quickfix

report:
	poetry run coverage report -m
