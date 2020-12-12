from flask import Flask, request
from flask-debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecret"
debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def index():

@app.route("/question/<num>")
def question_0(num):


