from flask import Flask, url_for
from flask import render_template
from flask import request
from classes import api_google
from classes import parser
from classes import api_wikipedia


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == "POST":
        search_post = request.get_data()
        my_apigoogle = api_google()
        my_apigoogle.init_api_maps()

        my_apigoogle.search_api_google(search_post)
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)