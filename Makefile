init: PYTHON-exists PYENV-exists PYENV-VIRTUALENV-exists
	pyenv install 3.7.1
	pyenv virtualenv 3.7.1 brisbane
	pyenv local brisbane
	pip install -r requirements.txt

test:
	nosetests tests

PYTHON-exists: ; @which python > /dev/null
PYENV-exists: ; @which pyenv > /dev/null
PYENV-VIRTUALENV-exists: ; @which pyenv-virtualenv > /dev/null
