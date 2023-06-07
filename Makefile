install: 
	poetry install
lint:
	poetry run flake8	
build: 
	poetry build
#publish: 
#	poetry publish --dry-run
package-install: 
	python3 -m pip install --force-reinstall --user dist/*.whl
