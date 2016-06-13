#! bash script for setting up enviornment for flask app

sudo apt-get install python-virtualenv

virtualenv flask

flask/bin/pip install flask

flask/bin/pip install flask-wtf

flask/bin/pip install selenium

flask/bin/pip install conf

flask/bin/pip install -U flask-cors
