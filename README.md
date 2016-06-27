# Semantic Style Sheets (SSS) Project
This project consists of multiple components. SSS Studio is one component of this SSS Project.

This repository contains SSS studio which can be used to highlight and modify a webpage as per your convineance

## SSS Studio - sssstudio
This web app is being developed in Python Virtual Environment using Flask. Before we execute the code found in this repository, we need to 

1. setup the environment in local system
2. config files
3. activate virtual environment wrapper
4. start the web application 
 
### setting up the environment
Python has a virtual environment concept which we need to setup. This is automatically setup in your local machine by running the `setup.sh` shellscript file

```sh
$ . setup.sh
```

### configuring files
Copy the conf file to a personal copy

```sh
$ cp sample_conf.py conf.py
```

In 'conf.py' file insert a string in the quotes. This will be your secret key. save this change using your favorite editor.

### Activate Virtual Environment
activate the virtual enviornment by

```sh
$ source flask/bin/activate
```

Now you should have a `(flask)` visible on your prompt.

### Start the web application

First we need to start the server.
```python
python app.py 
``` 

Once the server is running in your local host, goto that web page by typing this URL

```sh
127.0.0.1:8000
```

Now you have the app up and running.

