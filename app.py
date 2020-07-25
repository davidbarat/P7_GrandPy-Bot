from flask import Flask, url_for
from flask import render_template
from flask import request
from api import ApiGoogle
from parser import Parser
from api import ApiWikipedia
import sys


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == "POST":
        clean_data = ''
        search_post = request.get_data()
        # print('search_post -> ' + (search_post.decode('ascii')) )
        my_apigoogle = ApiGoogle()
        my_apigoogle.init_api_maps()

        myparser = Parser()
        clean_data = myparser.delete_stopwords(search_post.decode('ascii'))
        my_apigoogle.search_api_google(clean_data)
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)