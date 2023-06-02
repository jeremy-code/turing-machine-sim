# Define variables
PYTHON = python3
PIP = pip3
TEST_RUNNER = pytest
PACKAGE_NAME = my_package

# Define targets
.PHONY: install test clean

install:
	$(PIP) install -r requirements.txt

test:
	$(TEST_RUNNER) tests/

clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf src/__pycache__/
	rm -rf tests/__pycache__/


run:
	$(PYTHON) src/main.py