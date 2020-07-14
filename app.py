from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

@app.route('/search/', methods=['GET','POST'])
def test():
    # clicked = None
    if request.method == "POST":
        clicked = request.json['data']
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
