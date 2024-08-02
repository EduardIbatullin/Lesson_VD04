from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/new/")
def new():
    return "New page!"


if __name__ == "__main__":
    app.run()
