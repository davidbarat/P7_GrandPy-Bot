from flask import Flask, url_for
from flask import render_template
from flask import request
from classes import get_test

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    # if request.method == "POST":
        # input_data = request.get_data()
        # get_test(input_data)
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def test():
    if request.method == "POST":
        # print(request.json['data'])
        input_data = request.get_data()
        get_test(input_data)
        print("search")
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)