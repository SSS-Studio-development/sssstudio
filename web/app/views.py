from app import app
import requests
import bs4

@app.route("/translate/<word>", methods=['GET','POST','PUT'])
def trans(word):

    res = requests.get('http://www.phonemicchart.com/transcribe/?w='+word)
    soup = bs4.BeautifulSoup(res.text)
    ret = str(soup.select('center'))
    return ret
