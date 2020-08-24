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
my_apigoogle = ApiGoogle()
apiKey = my_apigoogle.getKey()
list_search = []


@app.route('/')
def index():
    return render_template('index.html', key=apiKey)

@app.route('/search', methods=['POST'])
def search():
    dict_response = {}
    # dict_response["search"] = [' ']
    search_post = request.get_data()
    clean_search_post = search_post.decode('utf-8')
    if clean_search_post and request.method == "POST":
        my_apiwiki = ApiWikipedia()
        myparser = Parser()
        clean_data = ''
        search_post_str = search_post.decode('utf-8')
        list_search.append(search_post_str)
        dict_response["search"] = list_search
        print(list_search)
        clean_data = myparser.delete_stopwords(search_post.decode('utf-8'))
        clean_data_string = ' '.join(clean_data)
        dict_response["lat"], dict_response["lng"], dict_response["key"] = my_apigoogle.search_api_google(
            clean_data_string)
        dict_response["summary"], dict_response["url"] = my_apiwiki.search_api_wikipedia(
            dict_response["lat"], dict_response["lng"])
        dict_response_dump = json.dumps(dict_response, ensure_ascii=False)
        print(dict_response_dump)
        return jsonify(dict_response)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)