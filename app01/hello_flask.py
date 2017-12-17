from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    """
    This is called a view function which serves the urls
    http://localhost:5000/
    http://localhost:5000/hello
    :return:
    """
    return "Hello World!"


if __name__ == '__main__':
    app.run()
