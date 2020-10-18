install:
	poetry install

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff/

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish -r oleglego94-Gendiff -u o_legleg_o

coverage:



.PHONY: install test lint selfcheck check build publish