.DEFAULT_GOAL := help
IS_CI:=$(CI)

help:             ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : test
test:             ## Run all the tests
test:
	python setup.py test

.PHONY : recreate_pyenv
recreate_pyenv:   ## Create the python environment. Recreates if the env exists already.
recreate_pyenv:
ifdef IS_CI
	@echo "************** Since this is CI server, appending conda-environment name with ${CI_JOB_ID} **********"
	@sed -i -e "s/idx-stream/idx-stream_${CI_JOB_ID}/g" dev_environment.yml
endif
	conda env create --force -f dev_environment.yml
