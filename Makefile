install:
	poetry install

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/ -vv

lint:
	poetry run flake8 gendiff tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish -r oleglego94-Gendiff -u o_legleg_o

.PHONY: install test lint selfcheck check build publish