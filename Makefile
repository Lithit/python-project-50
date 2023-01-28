install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

run-test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

gendiff-flat-json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json