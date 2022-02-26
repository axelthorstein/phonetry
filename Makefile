.PHONY: docs
init:
	pip install -r requirements.txt

test:
	pytest tests

autopep8:
	autopep8 --in-place --aggressive --aggressive --recursive phonetry/
