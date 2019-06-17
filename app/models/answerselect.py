"""Holds AnswerSelect model."""

import datetime

from .. import db


class AnswerSelect(db.Model):
    """Model to hold a users selected answers."""

    __tablename__ = "answerselects"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    answer_id = db.Column(db.Integer, db.ForeignKey("answers.id"))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship("User", backref="answerselects", lazy=True)
    answer = db.relationship("Answer", backref="answerselects", lazy=True)

    def __repr__(self):
        """Return string readable version of model."""
        return "<AnswerSelect {}:{}>".format(
            self.user.name,
            self.answer.text)
