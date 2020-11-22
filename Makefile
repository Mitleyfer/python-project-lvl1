install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
package-install:
	pip install --user dist/*.whl
package-uninstall:
	pip uninstall dist/*.whl
lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
