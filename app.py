from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import jsonify
from api import ApiGoogle
from parser import Parser
from api import ApiWikipedia
import sys
import json
import jinja2
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

dict_response = {}

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', dict_response = dict_response)

@app.route('/search', methods=['GET','POST'])
def search():
    my_apigoogle = ApiGoogle()
    my_apiwiki = ApiWikipedia()
    myparser = Parser()

    if request.method == "POST":
        clean_data = ''
        search_post = request.get_data()
        clean_search_post = search_post.decode('ascii')
        dict_response["search"] = clean_search_post
        
        clean_data = myparser.delete_stopwords(search_post.decode('ascii'))
        # a revoir moche le [0]
        dict_response["lat"], dict_response["lng"], dict_response["key"] = my_apigoogle.search_api_google(
            clean_data[0])
        
        dict_response["summary"], dict_response["url"] = my_apiwiki.search_api_wikipedia(
            dict_response["lat"], dict_response["lng"])
        dict_response_dump = json.dumps(dict_response, ensure_ascii=False)
        # return render_template('index.html', dict_response_dump=dict_response_dump)
        print(dict_response_dump)
        return jsonify(dict_response_dump)

    return render_template('index.html', dict_response = dict_response)


if __name__ == '__main__':
    app.run(debug=True)
    # app.config["TEMPLATES_AUTO_RELOAD"] = True