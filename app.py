from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecret"
debug = DebugToolbarExtension(app)
current_survey = surveys["satisfaction"]
current_question = 0

@app.route("/")
def index():
    return render_template("index.html", survey=current_survey)

@app.route("/start", methods=["POST"])
def start():
    session["responses"] = {}
    return redirect("/question/0")


@app.route("/question/<num>")
def question(num):
    global current_question
    num = int(num)
    if num != current_question:
        num = current_question
        flash("Invalid question. Please answer this question before moving on.")
        return redirect(f"/question/{num}")
    return render_template("question.html", survey=current_survey, num=num)

@app.route("/answers/<num>", methods=["POST"])
def answer(num):
    global current_question
    current_question += 1
    question = current_survey.questions[int(num)].question
    answer = request.form[question]
    print(request.form[question], "answer")
    responses = session["responses"]
    responses[question] = answer
    session["responses"] = responses
    return redirect(f"/question/{current_question}")

@app.route("/answers")
def answers():
    return render_template("answers.html", survey=current_survey)


    
