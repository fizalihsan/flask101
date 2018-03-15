# Flask tutorial

## Setup

* Create a virtualenv `python3 -m venv myvirtualenv`
* Activate the virtualenv: `source ~/Fizal/apps/myvirtualenv/bin/activate`
* To deactivate: `source ~/Fizal/apps/myvirtualenv/bin/deactivate`
* To export the dependencies to a file: `pip3 freeze > requirements.txt`
* To install the dependencies: `pip3 install -r requirements.txt`

* To start the flask process: `FLASK_APP=hello_flask.py flask run`