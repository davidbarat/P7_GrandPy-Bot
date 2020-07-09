from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
