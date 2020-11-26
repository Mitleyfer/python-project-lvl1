install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
package-install:
	pip3  install --user dist/*.whl
package-uninstall:
	pip3 uninstall dist/*.whl
rec:
	asciinema rec
lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
