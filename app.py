from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from flask import Flask, request, render_template, make_response, session, jsonify, g, url_for, send_from_directory, \
    redirect
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, ValidationError
from wtforms.validators import Required,URL
from flask_cors import CORS
import conf

app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = conf.SECRET_KEY[0]

# FORM for url
class url_form(Form):
    url = StringField('enter URL', validators=[Required(message="required"),URL(message="invalid input"),])
    submit = SubmitField("TagIt")


@app.route('/', methods=['GET','POST'])

# first page that will ask user to enter the URL
def index():

    form = url_form()
    if request.method == 'POST':
        if form.validate() == False:
            print "enter valid url"
            return render_template('index.html', form=form)  # if URL is invalid, it will return to index
        elif form.validate_on_submit():
            global url
            url = form.url.data
            print url
            abc = run_selenium(url) # redirecting to selenium to inject javascript and automate further process
            return redirect(abc)

    elif request.method == 'GET':
        return render_template('index.html', form = form, title="Home")


# selenium webdriver in use

def run_selenium(passed_url):
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    uas = request.user_agent.string

    if 'OPR' in uas:
        browser = 'Opera'
        driver = webdriver.Opera()
    elif browser == 'chrome':
        browser = 'Chrome'

        #locatio of chromedriver needed for running seenium on chrome browser. chromedriver is uploaded to github repo
        driver = webdriver.Chrome(conf.CHROME_DRIVER_PATH[0])
    elif browser == 'firefox':
        browser == 'Firefox'
        driver = webdriver.Firefox()  # for now works with firefox only

    print browser

    print (passed_url)

    driver.get(passed_url) #passing url taken from form
    print ("till here done")
    head_element = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_tag_name('head')) # waiting for page to atleast load <head> element fully so script could be injected
    print ("done till here")
    if head_element:
        print ("injecting script")

        # rawgit.com MaxCDN service used.. js file is at github repo annoletjs/master
<<<<<<< HEAD
        driver.execute_script("!function(){function e(){script=document.createElement('script'),script.type='text/javascript',script.src='//raw.githubusercontent.com/SSS-Studio-development/annoletjs/patch/annolet_main.js',document.getElementsByTagName('head')[0].appendChild(script)}($=window.jQuery)?e():(script=document.createElement('script'),script.src='//ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',script.onload=e,document.getElementsByTagName('head')[0].appendChild(script))}();")
=======
        driver.execute_script("!function(){function e(){script=document.createElement('script'),script.type='text/javascript',script.src='//rawgit.com/SSS-Studio-development/annoletjs/tagger/annolet_main.js',document.getElementsByTagName('head')[0].appendChild(script)}($=window.jQuery)?e():(script=document.createElement('script'),script.src='//ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',script.onload=e,document.getElementsByTagName('head')[0].appendChild(script))}();")
>>>>>>> 49f2a589805b9955bd5b9afb7be187a5a328e66d
        print ("injected")
    return 'annotate'
@app.route('/annotate')
def enjoy():
    return render_template('after_load.html', title='enjoy')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8000")
