SHELL = /bin/bash

define PROJECT_HELP_MSG
Usage:\n
  make help     \t show this message\n
  make clean    \t remove intermediate files (see CLEANUP)\n
  \n
  make ${VENV}  \t make a virtualenv in the base directory (see VENV)\n
  make install  \t install python packages in requirements.txt\n
  \n
  make tests    \t run listbuckets test script to list all S3 buckets\n
endef
export PROJECT_HELP_MSG

help:
	echo -e $$PROJECT_HELP_MSG | less

VENV = venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

${VENV}: venv
	virtualenv $@

install: requirements.txt | ${VENV}
	source ./${VENV}/bin/activate
	pip install -r requirements.txt
	pip install -e .

tests: tests/test_*.py
	pytest -vv tests

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: tests install configure clean
