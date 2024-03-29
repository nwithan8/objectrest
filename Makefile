PYTHON_BINARY := python3
VIRTUAL_ENV := venv
VIRTUAL_BIN := $(VIRTUAL_ENV)/bin
PROJECT_NAME := objectrest
TEST_DIR := tests

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## build - Builds the project in preparation for release
build:
	$(PYTHON_BINARY) setup.py sdist bdist_wheel

## coverage - Test the project and generate an HTML coverage report
coverage:
	$(VIRTUAL_BIN)/pytest --cov=$(PROJECT_NAME) --cov-branch --cov-report=html --cov-report=term-missing

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf $(VIRTUAL_ENV)
	find . -name '*.pyc' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

## black - Runs the Black Python formatter against the project
black:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/

## black-check - Checks if the project is formatted correctly against the Black rules
black-check:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/ --check

## format - Runs all formatting tools against the project
format: black lint

## format-check - Checks if the project is formatted correctly against all formatting rules
format-check: black-check lint

## install - Install the project locally
install:
	$(PYTHON_BINARY) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_BIN)/pip install -e ."[dev]"

## lint - Lint the project
lint:
	$(VIRTUAL_BIN)/flake8 $(PROJECT_NAME)/ $(TEST_DIR)/

## test - Test the project
test:
	$(VIRTUAL_BIN)/pytest

.PHONY: help build coverage clean black black-check format format-check install lint test