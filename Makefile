
lint:
	pylint ./slib ./test ./server run.py

coverage:
	coverage run -m unittest discover -s ./ -p "*_tests.py"
	coverage report -m
	coverage html

coverage_branch:
	coverage run --branch -m unittest discover -s ./ -p "*_tests.py"
	coverage report -m
	coverage html

test_all:
	python -m unittest discover -s ./ -p "*_tests.py"