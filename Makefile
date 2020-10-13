install:
	poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff/

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish -r oleglego94-Gendiff -u o_legleg_o


.PHONY: install test lint selfcheck check build