# from datetime import datetime
import json

from flask import (
    render_template, session, redirect, url_for, abort
)
from . import main
from .forms import LoginForm
from .. import db
from .. import models
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user = User(name=form.name.data)
            db.session.add(user)
            db.session.commit()

        session['user'] = user.name
        session['user_id'] = user.id
        return redirect(url_for('.quizzes'))
    return render_template("index.html", form=form)


@main.route('/example/')
def example():
    return session['user']


@main.route('/quizzes/')
def quizzes():
    # TODO: filter quizes user has already done
    quizzes = models.Quiz.query.all()
    return render_template("quizzes.html", quizzes=quizzes)


@main.route('/quizzes/<quiz_id>')
def quiz(quiz_id):
    quiz = models.Quiz.query.filter_by(id=quiz_id).first()
    user = get_user()
    done_questions = models.AnswerSelect.query.filter_by(
        user_id=user.id, quiz_id=quiz.id).all()
    done_ids = [d.question_id for d in done_questions]

    done_qs = []  # This should also be a generator
    for qs in quiz.questions:
        if qs.id in done_ids:
            done_qs.append(qs.id)
    print(done_qs)
    if not quiz:
        abort(404)

    return render_template("quiz.html", quizz=quiz, done_qs=done_qs)


@main.route('/questions/<question_id>')
def question(question_id):
    question = models.Question.query.filter_by(id=question_id).first()

    if not question:
        abort(404)

    return render_template("question.html", question=question)


@main.route('/question_answer/<answer_id>', methods=['POST'])
def question_answer(answer_id):
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
    # TODO should be a class method on user model
    return models.User.query.filter_by(id=session['user_id']).first()
