
lint:
	pylint ./slib ./test main.py

coverage:
	coverage run -m unittest discover -s ./ -p "*_test.py"
	coverage report -m
	coverage html

coverage_branch:
	coverage run --branch -m unittest discover -s ./ -p "*_test.py"
	coverage report -m
	coverage html

test_all:
	python -m unittest discover -s ./ -p "*_test.py"