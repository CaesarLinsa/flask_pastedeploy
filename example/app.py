from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello world"

app.config.from_pyfile('config')
