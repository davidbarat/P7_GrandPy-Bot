import flask
app = flask.Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
