#! bash script for setting up enviornment for flask app

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python-virtualenv|grep "install ok installed")
echo Checking for python-virtualenv: $PKG_OK
if [ "" == "$PKG_OK" ]; then
      echo "No python-virtualenv. Setting up python-virtualenv."
        sudo apt-get install python-virtualenv
fi

virtualenv flask

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' flask|grep "install ok installed")
echo Checking for flask: $PKG_OK
if [ "" == "$PKG_OK" ]; then
      echo "No flask. Setting up flask."
      flask/bin/pip install flask
fi




PKG_OK=$(dpkg-query -W --showformat='${Status}\n' flask-login|grep "install ok installed")
echo Checking for some: $PKG_OK
if [ "" == "$PKG_OK" ]; then
      echo "No flask-login . Setting up flask-login"
      flask/bin/pip install flask-login
fi



PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python-requests|grep "install ok installed")
echo Checking for python-requests: $PKG_OK
if [ "" == "$PKG_OK" ]; then
      echo "No python-requests. Setting up python-requests."
      flask/bin/pip install requests
fi
