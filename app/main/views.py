"""Main application end points."""
import json

from flask import (
    render_template, session, redirect, url_for, abort
)
from . import main
from .forms import LoginForm
from .. import db
from .. import models
from random import randint  # TODO remove


@main.route("/", methods=["GET", "POST"])
def index():
    """App entry point.

    Consists of login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(name=form.name.data).first()
        if user is None:
            user = models.User(name=form.name.data)
            db.session.add(user)
            db.session.commit()

        session["user"] = user.name
        session["user_id"] = user.id
        return redirect(url_for(".quizzes"))
    return render_template("index.html", form=form)


@main.route("/quizzes/")
def quizzes():
    """Get a list of all accessable quizes."""
    # TODO: filter quizes user has already done
    quizzes = models.Quiz.query.all()
    return render_template("quizzes.html", quizzes=quizzes)


@main.route("/quizzes/<quiz_id>")
def quiz(quiz_id):
    """Return a single quiz."""
    quiz = models.Quiz.query.filter_by(id=quiz_id).first()
    user = get_user()
    done_questions = models.AnswerSelect.query.filter_by(
        user_id=user.id, quiz_id=quiz.id).all()

    # which questions have been completed
    done_ids = [d.question_id for d in done_questions]
    done_qs = [qs.id for qs in quiz.questions if qs.id in done_ids]

    quiz_done = (quiz.question_count == len(done_qs))

    if not quiz:
        abort(404)

    return render_template(
        "quiz.html", quizz=quiz, done_qs=done_qs, quiz_done=quiz_done)


@main.route("/questions/<question_id>")
def question(question_id):
    """Return a single question."""
    question = models.Question.query.filter_by(id=question_id).first()

    if not question:
        abort(404)

    return render_template("question.html", question=question)


@main.route("/question_answer/<answer_id>", methods=["POST"])
def question_answer(answer_id):
    """Log a users answer to a question."""
    answer = models.Answer.query.filter_by(id=answer_id).first()
    user = get_user()
    if not answer:
        abort(404)

    question_id = answer.question.id
    quiz_id = answer.question.quiz.id
    selection = models.AnswerSelect(
        user=user, quiz_id=quiz_id, question_id=question_id, answer=answer)
    db.session.add(selection)
    db.session.commit()

    if answer.is_correct:
        return json.dumps({"correct": True})
    else:
        return json.dumps({"correct": False})


def get_user():
    """Get current user object."""
    # TODO should be a class method on user model
    # @property?
    return models.User.query.filter_by(id=session["user_id"]).first()


@main.route("/result_report/", methods=["GET"])
def result_report():
    """Report of completed quizzes.

    TODO
    Details of all the quizzes completed and how many people scored within
    each 10% increment of the quiz. The script will be triggered as a
    scheduled task using a container orchestration service.
    """
    quizzes = models.Quiz.query.all()
    report = {q.name: randint(1, 10) for q in quizzes}

    return json.dumps(report)
